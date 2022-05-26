import gpxpy
import pandas as pd
import geopandas as gpd
import __meta__ as meta
import os
import matplotlib.pyplot as plt
import uuid
import warnings
from math import acos, cos, sin, radians
from shapely.geometry import Point

warnings.filterwarnings("ignore")


class AnalyzeGpx:

    def __init__(self, app):
        self.__app = app
        self.__last_latitude = 0
        self.__last_longitude = 0
        self.__last_distance = 0
        self.__start_process = True
        self.__uuid = uuid.uuid1()

    def __distance_between_points(self, point_1: tuple, point_2: tuple) -> float:
        """allows to calculate distance between two points using
           Haversine, reference https://en.wikipedia.org/wiki/Haversine_formula
        Args:
            point_1 (tuple): coordinates system # 1
            point_2 (tuple): coordinates system # 2

        Returns:
            float: distance in kilometers
        """

        value = 0.0
        try:
            point_1 = (radians(point_1[0]), radians(point_1[1]))
            point_2 = (radians(point_2[0]), radians(point_2[1]))
            distance = acos(sin(point_1[0]) * sin(point_2[0]) +
                            cos(point_1[0]) * cos(point_2[0]) * cos(point_1[1] - point_2[1]))
            value = distance * 6371.01
        except Exception as ex:
            self.__app.logger.error(ex)
            value = self.__app.constants.ERROR
        return value

    def __read_gpx(self, file: str) -> pd.DataFrame:
        """allows to read gpx file and generate dataframe

        Args:
            file (str): gpx file to analyze

        Returns:
            pd.DataFrame: xml to pandas dataframe
        """
        df = None
        points = []
        with open(file) as f:
            gpx = gpxpy.parse(f)

        for segment in gpx.tracks[0].segments:
            for p in segment.points:
                points.append({
                    'time': p.time,
                    'latitude': p.latitude,
                    'longitude': p.longitude,
                    'elevation': p.elevation
                })
        df = pd.DataFrame.from_records(points)
        return df

    def __coordinates_validation(self, row):
        """allows to generate new fields and calculate the distance

        Args:
            row (df.row): dataframe row

        Returns:
            row: dataframe row with the new transformation
        """
        distance = 0
        tag = ""
        if self.__start_process:
            tag = "START"
            distance = 0
            self.__last_distance = distance
            self.__start_process = False
            row["end_latitude"] = row.latitude
            row["end_longitude"] = row.longitude
            self.__last_latitude = row.latitude
            self.__last_longitude = row.longitude
        elif (self.__last_latitude == row.latitude) and (self.__last_longitude == row.longitude):
            tag = "WAITING"
            distance = self.__last_distance
            row["end_latitude"] = self.__last_latitude
            row["end_longitude"] = self.__last_longitude
        else:
            point_1 = (self.__last_latitude, self.__last_longitude)
            point_2 = (row.latitude, row.longitude)
            distance = self.__distance_between_points(point_1, point_2)
            row["end_latitude"] = self.__last_latitude
            row["end_longitude"] = self.__last_longitude
            self.__last_latitude = row.latitude
            self.__last_longitude = row.longitude
            tag = "SHIFT"

        row["distance"] = distance
        row["tag"] = tag
        return row

    def __transformations(self, df):
        """Allow to add extra fields validation that will be used by spark.

        Args:
            df (df): dataframe

        Returns:
            df: dataframe row with the new transformation
        """
        df = df.apply(self.__coordinates_validation, axis=1)
        df['time'] = pd.to_datetime(df['time'], format='%Y%m%d').dt.tz_localize(None)
        df['mark_time'] = pd.to_datetime(df['time']).dt.strftime('%Y%m%d')
        df['year'] = pd.DatetimeIndex(df['time']).year
        df['month'] = pd.DatetimeIndex(df['time']).month
        df['day'] = pd.DatetimeIndex(df['time']).day
        df['hour'] = pd.DatetimeIndex(df['time']).hour
        df['minute'] = pd.DatetimeIndex(df['time']).minute
        df['second'] = pd.DatetimeIndex(df['time']).second
        df["vehicle_type"] = self.__app.args.vehicle_type
        df["vehicle_id"] = self.__app.args.vehicle_id

        df.columns = [
            "event_date",
            "start_latitude",
            "start_longitude",
            "elevation",
            "end_latitude",
            "end_longitude",
            "distance",
            "tag",
            "event_mark_time",
            "event_year",
            "event_month",
            "event_day",
            "event_hour",
            "event_minute",
            "event_second",
            "vehicle_type",
            "vehicle_id"
        ]

        df = df[[
            "vehicle_id",
            "vehicle_type",
            "event_date",
            "event_year",
            "event_month",
            "event_day",
            "event_hour",
            "event_minute",
            "event_second",
            "event_mark_time",
            "start_latitude",
            "start_longitude",
            "end_latitude",
            "end_longitude",
            "distance",
            "tag",
            "elevation"
        ]]
        return df

    def __create_geometry(self, row):
        """allows to generate geometry field to geopandas, see
        https://shapely.readthedocs.io/en/stable/manual.html

        Args:
            row (df.row): dataframe row

        Returns:
            _type_: dataframe row with the new transformation
        """
        row["geometry"] = Point(row["start_longitude"], row["start_latitude"])
        return row

    def __generate_map(self, df):
        """allows to introduce multi-polygon and generating maps
        with the points getting of gpx file

        Args:
            df (df): dataframe with info taken of gpx file
        """
        cities = gpd.read_parquet(os.path.join(meta.__basemaps__, self.__app.config.cities_delimited))
        roads = gpd.read_parquet(os.path.join(meta.__basemaps__, self.__app.config.roads_delimited))
        points = df.apply(self.__create_geometry, axis=1)
        gpd_points = gpd.GeoDataFrame(points, crs="EPSG:4326")

        fig, ax = plt.subplots(1, 1, figsize=(20, 20))
        roads.plot(ax=ax, color="#524A4A", lineWidth=0.3, alpha=0.5)
        cities.plot(ax=ax, color="#F1ECEB", alpha=0.7)
        gpd_points.plot(ax=ax, markersize=40, color="red", alpha=0.5, edgecolor="white", marker=".", lineWidth=0.7)
        title = "EVENT DATE: {} | ID: {} | TYPE: {}".format(
            self.__app.args.event_date,
            self.__app.args.vehicle_id,
            self.__app.args.vehicle_type
        )
        plt.title(title)
        plt.axis("off")
        plt.axis("equal")
        plt.legend(["highway", "points"], loc=0, frameon=True)
        plt.savefig(os.path.join(self.__app.args.output, "images", f'{self.__uuid}.png'))

    def start(self):
        """main public class method
        """
        self.__app.logger.info("reading gpx file..")
        df = self.__read_gpx(self.__app.args.gpx)
        self.__app.logger.info("etl with pandas..")
        df = self.__transformations(df)
        self.__app.logger.info("creating maps with geopandas..")
        self.__generate_map(df)
        self.__app.logger.info("saving data..")
        df.to_parquet(os.path.join(self.__app.args.output, "files", f'{self.__uuid}.parquet'))
