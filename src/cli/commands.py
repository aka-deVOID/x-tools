from abc import ABC, abstractmethod

from .abstracts import AbstractMenu, AbstractCommand


class HelpCommand(AbstractCommand):
    def exec(self) -> AbstractMenu:
        print("hello")
        return self.menu


class BrowserKeepAliveCommand(HelpCommand):
    def exec(self) -> AbstractMenu:
        return self.menu
