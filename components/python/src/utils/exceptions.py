

class BadConfigValidatorError(Exception):
    """
        class that allow to you customize the exception when the program has
        a bad configuration
    """
    pass


class JsonNotFound(Exception):
    """
        class that allow to you customize the exception when the json
        doesn't exist
    """
    pass


class LoggerValidatorNotFound(Exception):
    """
        class that allow to you customize the exception when logger
        configuration
        instance is bad.
    """
    pass


class InvalidConfigContent(Exception):
    """
        class that allow to you customize the config content file .
    """
    pass


class ModuleOrClassNotFound(Exception):
    """
        class that allow to you customize if exists a module
    """
    pass
