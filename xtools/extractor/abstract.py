from abc import ABC

from xtools.core import Driver


class ElementAbstract(ABC):
    def __init__(self):
        self.__driver = Driver()
