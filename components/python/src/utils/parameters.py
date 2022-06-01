import argparse
import os
import sys


def exist_file(value):
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError("file {} doesn't exist, check please.".format(value))
    return value


def exist_dir(value):
    if not os.path.isdir(value):
        raise argparse.ArgumentTypeError("dir {} doesn't exist, check please.".format(value))
    return value


def get_args():

    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        title="Demo python, spark project",
        metavar="simple data processing demo",
        dest="command"
    )
    parser_file = subparsers.add_parser('run-process', help="execute processing data")
    parser_file.add_argument(
        '--gpx-file', dest="gpx",
        type=exist_file,
        required=True,
        help="gpx file to analyze and extract data"
    )
    parser_file.add_argument(
        '--vehicle-type',
        dest="vehicle_type",
        type=str, required=True,
        help="vehicle type that will be processed"
    )
    parser_file.add_argument(
        '--vehicle-id',
        dest="vehicle_id",
        type=str,
        required=True,
        help="vehicle id that belong the data"
    )
    parser_file.add_argument(
        '--event-date',
        dest="event_date",
        type=str,
        required=True,
        help="event date related to file"
    )
    parser_file.add_argument(
        '--output',
        dest="output",
        type=exist_dir,
        required=True,
        help="location where will be saved the data"
    )
    parser_report = subparsers.add_parser('generate-report', help="report and consolidation process")
    parser_report.add_argument(
        '--images-path', dest="images_path",
        type=exist_dir,
        required=True,
        help="gpx file to analyze and extract data"
    )
    parser_report.add_argument(
        '--consolidated-file',
        dest="consolidate_file",
        type=exist_file,
        required=True,
        help="vehicle type that will be processed"
    )

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()
    return parser
