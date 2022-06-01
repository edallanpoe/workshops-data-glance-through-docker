
import os.path

from src.models.application import Validator
from src.config.read import Config
from src.utils.constants import Constants
from src.utils.classesutil import Struct
from src.utils.generals import Python

__app__: str = "base project"
__basedir__: str = os.path.dirname(os.path.abspath(__file__))
__basemaps__: str = os.path.join("/".join(__basedir__.split("/")[:-2]), "data", "maps")
__baseresults__: str = os.path.join("/".join(__basedir__.split("/")[:-2]), "data", "output", "results")
__baseconfig__: str = os.path.join("/".join(__basedir__.split("/")[:-2]), "data", "parametric")
__version__: str = "1.0"
__release__: str = "0.0.0"
__description__: str = "simple base python project"


def get_app_instances():

    model = Validator()
    model.constants = Constants()
    model.config = Config()
    model.config = Struct(
        **model.config.get_config_app(
            model.config.CONFIG,
            model.keys.CONFIGFILE
        )
    )
    model.util = Python()
    model.logger = model.util.get_logger(
        app_name=__app__,
        log_name="docker-spark",
        log_location=model.constants.BASELOG
    )
    return model
