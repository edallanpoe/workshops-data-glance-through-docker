from tabnanny import verbose
import pandas as pd
import jinja2
import pdfkit
import os
import math
import plotly.graph_objects as go
import __meta__ as meta
from datetime import datetime
from PIL import Image
from plotly.subplots import make_subplots


class GeneratePdf:

    def __init__(self, app):
        self.__app = app
        self.__IMAGE_COLUMN = self.__app.config.images.get("columns")
        self.__IMAGE_SIZE = self.__app.config.images.get("size")
        self.__IMAGE_ROW = 0
        self.__NUM_COMPLEMENTS = 0

    def __create_pdf(self, template_path: str, pdf_info: dict):
        template_name = template_path.split("/")[-1]
        template_path = template_path.replace(template_name, "")
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))
        template = environment.get_template(template_name)
        html = template.render(pdf_info)
        config = pdfkit.configuration(wkhtmltopdf=self.__app.config.wkhtmltopdf)
        pdfkit.from_string(
            html,
            pdf_info["pdf"],
            options=self.__app.config.pdf_properties,
            configuration=config,
            verbose=True
        )

    def __get_rows_complements(self, nro_images: int):
        rows = 0
        complements = 0
        columns = nro_images if nro_images < self.__IMAGE_COLUMN else self.__IMAGE_COLUMN
        operation = nro_images / columns
        if operation.is_integer():
            rows = int(operation)
        else:
            frac, whole = math.modf(operation)
            analyze = 1 - frac
            complements = int(analyze / 0.25)
            rows = int(whole) + 1
        return rows, columns, complements

    def __image_compose(self, image_names: list, maps_merged_path: str):
        to_image = Image.new(
            'RGB',
            (
                self.__IMAGE_COLUMN * self.__IMAGE_SIZE,
                self.__IMAGE_ROW * self.__IMAGE_SIZE
            )
        )
        for y in range(1, self.__IMAGE_ROW + 1):
            for x in range(1, self.__IMAGE_COLUMN + 1):
                from_image = Image.open(
                    image_names[self.__IMAGE_COLUMN * (y - 1) + x - 1]
                ).resize((self.__IMAGE_SIZE, self.__IMAGE_SIZE), Image.ANTIALIAS)
                to_image.paste(from_image, ((x - 1) * self.__IMAGE_SIZE, (y - 1) * self.__IMAGE_SIZE))
        to_image.save(maps_merged_path)

    def __generate_plot(self, plot_path):
        df = pd.read_parquet(self.__app.args.consolidate_file)
        df['date'] = pd.to_datetime(df['event_date'], format='%Y%m%d')
        fig = make_subplots(
            rows=2,
            cols=2,
            subplot_titles=[
                "KM CONSUMED BY VEHICLE TYPE",
                "CONSUMED PER DAY",
                "KILOMETERS PER DAY",
                "KILOMETERS BY VEHICLE"],
        )
        fig.add_trace(go.Bar(x=df["vehicle_type"], y=df["km"], name='veh type vs km'), row=1, col=1)
        fig.add_trace(go.Bar(x=df["date"], y=df["consume_per_day"], name='date vs consume $'), row=1, col=2)
        fig.add_trace(go.Bar(x=df["date"], y=df["km"], name='date vs km'), row=2, col=1)
        fig.add_trace(go.Scatter(x=df["vehicle"], y=df["km"], name='veh x km', mode='markers'), row=2, col=2)
        fig.write_image(plot_path)

    def start(self):
        self.__app.logger.info("getting images..")
        files = os.listdir(self.__app.args.images_path)
        image_names = [os.path.join(self.__app.args.images_path, maps) for maps in files]
        maps_merged_path: str = os.path.join(meta.__baseresults__, "pictures", "maps_consolidated.png")
        plot_path: str = os.path.join(meta.__baseresults__, "pictures", "chart.png")
        html_template_path: str = os.path.join(meta.__baseconfig__, "templates", "template.html")
        pdf_path: str = os.path.join(meta.__baseresults__, "pdf", "report.pdf")
        vehicles_processed: int = len(image_names)

        self.__app.logger.info("calculating dynamic rows and columns..")
        self.__IMAGE_ROW, self.__IMAGE_COLUMN, self.__NUM_COMPLEMENTS = self.__get_rows_complements(len(files))
        for idx in range(self.__NUM_COMPLEMENTS):
            image_names.append(os.path.join(meta.__baseconfig__, "withe.jpg"))

        self.__app.logger.info("merging images..")
        self.__image_compose(image_names, maps_merged_path)

        self.__app.logger.info("generating plot..")
        self.__generate_plot(plot_path)
        pdf_info = {
            "merged": f"file://{maps_merged_path}",
            "pdf": pdf_path,
            "date_report": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            "vehicles": vehicles_processed,
            "plot": f"file://{plot_path}",
            "sponsor": self.__app.config.logo_sponsor
        }
        self.__app.logger.info("generating pdf..")
        self.__create_pdf(html_template_path, pdf_info)
