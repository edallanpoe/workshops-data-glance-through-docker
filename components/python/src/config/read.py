import json
from src.utils.exceptions import BadConfigValidatorError
import pkg_resources


class Config(object):
    """
      class that allows to recover the different system configurations
      statically and dynamically from .json files
    """
    def __init__(self):
        """
          class constructor

          parameters :
              msm  : object with the messages configured by language
              note: the file must be in the config module

          output :
              N/A

          usage:

              >>> from config.read import Config
              >>> config = Config()
       """
        self.__msm = None
        self.__msmcore = "[FATAL ERROR] configuracion principal no encontrada. por favor, contacte al administrador "

    @property
    def CONFIG(self):
        return "src.config.app"

    def get_config_app(self, config_path: str, config_file: str, error_message: str = ""):
        """
          allows to get the configuration data from a configuration file

          parameters :
             config_path :  config section to evaluate

          outputs :
              contenct in dict of json file

          usage :

              >>> from config.read import Config
              >>> config= Config()
              >>> config = get_config("")
              >>> print(config)
                  {key:value,....keyn:valuen}
        """
        data = {}
        try:
            with open(pkg_resources.resource_filename(config_path, config_file)) as config:
                data = json.load(config)
        except Exception:
            if error_message != "":
                raise BadConfigValidatorError(error_message)
            else:
                raise BadConfigValidatorError(self.__msmcore)
        return data
