#!/bin/python


class Validator:

    """
        Awoll to validate diferents rules associated to data.
        Each rule is defined by user
    """
    def __init__(self):
        """
            class constructor

            parameters : N/A
            output     : N/A

            usage:
                >>> from models.validator import Validator
                >>> validator = Validator()
                >>> ...
        """
        self.__python_util = None
        self.__constants = None
        self.__msm = None
        self.__keys = None
        self.__logger = None
        self.__args = None
        self.__config = None
        self.__bussiness = None
        self.__demo = None

    @property
    def util(self):
        """
           allows to return the value for the utilities

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from libraries.generals import Python
                >>> from models.validator import Validator
                >>> util_python = Python()
                >>> variable = util_python.util
        """
        return self.__python_util

    @util.setter
    def util(self, util):
        """
            allows setting the util instance

            parameters :
                util : util instance

            outputs :
                N/A

            usage :

                >>> from libraries.generals import Python
                >>> from models.validator import Validator
                >>> validator = Validator()
                >>> util_python = Python()
                >>> validator.util = util_python
        """
        self.__python_util = util

    @property
    def constants(self):
        """
           allows to return the value for the constants

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> variable = validator_dto.constants
        """
        return self.__constants

    @constants.setter
    def constants(self, constants):
        """
            allows setting the constants instance

            parameters :
                constants : constants instance

            outputs :
                N/A

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> validator_dto.constants = python_util.constants()
        """
        self.__constants = constants
        self.__keys = self.__constants._KEYS

    @property
    def keys(self):
        """
           allows to return the value for global keys

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> variable = validator_dto.keys
        """
        return self.__keys

    @property
    def logger(self):
        """
           allows to return the value for the logger

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> variable = validator_dto.logger"""
        return self.__logger

    @logger.setter
    def logger(self, logger):
        """
            allows setting the logger instance

            parameters :
                logger : logger instance

            outputs :
                N/A

            usage :

                >>> from libraries.generals import Python
                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> python_util = Python()
                >>> validator_dto.logger=python_util.\
                    logger("logs","APlicacionTest","/logs/test")
        """
        self.__logger = logger

    @property
    def args(self):
        """
           allows to return the value for the console args

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> variable = validator_dto.args
        """
        return self.__args

    @args.setter
    def args(self, args):
        """
            allows setting the argparse instance

            parameters :
                args : argparse instance

            outputs :
                N/A

            usage :

                >>> import argparse
                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> parser = argparse.ArgumentParser()
                >>> parser.add_argument('--foo', help='foo help')
                >>> validator_dto.args =parser.parse_args()
        """
        self.__args = args

    @property
    def config(self):
        """
           allows to return the value for the config instane

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> validator_dto = Validator()
                >>> variable = validator_dto.config
        """
        return self.__config

    @config.setter
    def config(self, config):
        """
           allows to set the value for the config instance

            parameters :
                N/A

            outputs :
                instance or configuration value

            usage :

                >>> from models.validator import Validator
                >>> from src.config.read import Config
                >>> validator_dto = Validator()
                >>> validator_dto.config = Config()
        """
        self.__config = config
