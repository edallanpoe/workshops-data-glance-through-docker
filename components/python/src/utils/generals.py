#!/bin/python
import sys
import os
import logging
import json
from datetime import datetime
from logging import handlers
from src.utils.exceptions import JsonNotFound


class Python:
    """
        class that allows generating utility python methods
        transversal to the whole process
    """
    def __init__(self):
        """
            class constructor:

            args:
                N/A
            output :
                N/A
            usage:
                >>> from utils.Python import Python
                >>> util = Python()
                >>> util.someMethod(..)
        """
        self.__log_path = None

    def get_logger(self, app_name: str,
                   log_name: str, log_location: str = "/tmp/logs",
                   log_format: str = "%Y%m%d%H%M%S", logger_level: int = 10):
        """
            It allows resetting the instance and configuration
            logger file, with the necessary structure format to
            allow storage and printing
            on the console at
            the same time.

            Note: he will validate the base directories,
            if they do not exist, create

            args:
                app_name : name of the application that is running
                log_name : segment of the name of the log, it is commonly the
                                    name of the app

            outputs :
                logger : returns the instance of a logger object ready
                         to be invoked or
                None if inconsistencies occur.

            usage :

                >>> from src.generals import Python
                >>> util = Python()
                >>> logger = util.get_logger(
                    "logs","APlicacionTest","/logs/test")
                >>> logger.debug('This is a debug message')
                2019-09-04 14:59:39,563 - [DEBUG] - [APlicacionTest]
                >>> logger.info('This is an info message')
                2019-09-04 15:00:38,083 - [INFO] - [APlicacionTest]
                >>> logger.warning('This is a warning message')
                2019-09-04 15:00:38,083 - [WARNING] - [APlicacionTest]
                >>> logger.error('This is an error message')
                2019-09-04 15:00:38,083 - [ERROR] - [APlicacionTest]
                >>> logger.critical('This is a critical message')
                2019-09-04 15:00:38,083 - [CRITICAL] - [APlicacionTest]

                Notes :
                    1. you can see the contents of the file with cat o vi
                       TestLoger_......log
                    2. logs level : CRITICAL=50,ERROR=40,WARNING=30,INFO=20,
                       DEBUG=10,NOTSET=0
        """
        self.create_base_folders(log_location)
        log_save = os.path.join(
            log_location,
            (app_name or "UnknowNameLog") + "_{}.log".format(datetime.now().strftime(log_format)))
        self.__log_path = log_save
        logger = None
        try:
            logger = logging.getLogger(log_name or "UnknowApp")
            logger.setLevel(logger_level)
            format = logging.Formatter(
                "%(asctime)s - [%(levelname)s] - [%(name)s] : %(message)s")
            loginStreamHandler = logging.StreamHandler(sys.stdout)
            loginStreamHandler.setFormatter(format)
            logger.addHandler(loginStreamHandler)

            fileHandler = handlers.RotatingFileHandler(
                log_save, maxBytes=(1048576 * 5), backupCount=7)
            fileHandler.setFormatter(format)
            logger.addHandler(fileHandler)
        except Exception:
            logger = None
        return logger

    def create_base_folders(self, path: str, subfolders: str = ""):
        """
        It allows you to create folders in a specific directory from string,
        which supports several folders separated by ","

        Notes:
            1. if the folder exists, it does not execute the creation command
            2. if sub folders is empty, only will create the path

        args:

            path       : path where folders will be created
                sub folders : string with folders to create inside the forlder

        outputs :
            N/A

        usage :

            >>> from src.generals import Python
            >>> util = Python()
            >>> util.create_base_folders("/tmp","config,libraries,logs,sqls")

            tree
                * config
                * libraries
                * logs
                * sqls
        """
        if subfolders == "" or subfolders is None:
            if not os.path.exists(path):
                os.mkdir(path)
        else:
            if not os.path.exists(path):
                os.mkdir(path)
            for folder in subfolders.split(","):
                if not os.path.exists(os.path.join(path, folder)):
                    os.mkdir(os.path.join(path, folder))

    def read_json(self, json_file: str, error_message: str):
        """
            allows to read a json file

        Args:
            json_file     (str): json path
            error_message (str): message error defined by user

        Raises:
            JsonNotFound: _description_

        Returns:
            _type_: _description_
        """
        data = {}
        try:
            with open(json_file) as config:
                data = json.load(config)
        except Exception:
            raise JsonNotFound(error_message)
        return data
