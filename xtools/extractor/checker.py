from __future__ import annotations
from selenium.webdriver import Firefox, Chrome


class Checker:
    def __init__(self, driver: Firefox | Chrome):
        self.__driver = driver
