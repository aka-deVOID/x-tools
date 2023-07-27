from abc import ABC, abstractmethod

from .abstracts import AbstractMenu, AbstractCommand
from core.driver import Driver


class HelpCommand(AbstractCommand):
    def exec(self) -> AbstractMenu:
        print("hello")
        return self.menu


class BrowserKeepAliveCommand(HelpCommand):
    def exec(self) -> AbstractMenu:
        Driver("firefox").keep_alive(True)
        print("browser keep alive is On.")
        return self.menu
