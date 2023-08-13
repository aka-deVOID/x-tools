from abc import ABC, abstractmethod

from .abstracts import AbstractMenu, AbstractCommand
from .core import Driver


class HelpCommand(AbstractCommand):
    def exec(self) -> AbstractMenu:
        # TODO: write some help for user hows this script works
        return self.menu


class BrowserKeepAliveCommand(AbstractCommand):
    def exec(self) -> AbstractMenu:
        driver = Driver()
        if driver.keep_alive:
            driver.keep_alive = False
            self.cmd_print("keep alive set OFF.")
        else:
            driver.keep_alive = True
            self.cmd_print("keep alive set ON.")
        return self.menu


class BrowserLoggingCommand(AbstractCommand):
    def exec(self) -> AbstractMenu:
        driver = Driver()
        return self.menu
