#!/bin/python


class Struct:
    """
    It allows through its constructor to send a dictionary and
    return an object structured with dictionary attributes.
    """

    def __init__(self, **config: dict):
        """
        class constructor Struct

        parameters :

            config : dictionary with the values
        outputs :
            struct objet

        usage:

            >>> from src.utils import Struct
            >>> structure = Struct({'version':'1.0','createdby':'luis'})
            >>> structure.version
            1.0
            >>> structure.createdby
            luis
        """
        self.__dict__.update(config)
