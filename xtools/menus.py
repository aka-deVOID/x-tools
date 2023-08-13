from __future__ import annotations
import sys
from typing import Any

from .abstracts import AbstractMenu, AbstractCommand
from .commands import HelpCommand, BrowserKeepAliveCommand, BrowserLoggingCommand  # cause cycle error
from .core import *


class FirefoxDriverMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                return BrowserKeepAliveCommand(self).exec()
            case 2:
                return BrowserLoggingCommand(self).exec()
            case 3:
                return self.back()
            case 5:
                self._exit()

    def print_menu(self) -> None:
        print("Select your option:")
        print("""[1] - Keep Alive (default Disable)
[2] - Browser Logging (default Disable)
[3] - Back
[5] - Exit""")

    def push(self, data: Any) -> None:
        pass


class FirefoxOptionMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                pass
            case 2:
                self._exit()
            case _:
                pass

    def push(self, data: Any) -> None:
        pass

    def print_menu(self) -> None:
        pass


class ToolsMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                return self.back()
            case 7:
                self._exit()

    def print_menu(self) -> None:
        print("Select One Option:")
        print(
            "[1] - Delete Tweets (+Medias)\n[2] - Delete Medias\n[3] - Delete Replies\n[4] - Remove Likes\n[5] - Remove Followings\n[6] - Prev Menu\n[7] - Exit"
        )

    def push(self, data: Any) -> None:
        pass


class FirefoxMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                return FirefoxDriverMenu(self)
            case 2:
                return FirefoxOptionMenu(self)
            case 3:
                return ToolsMenu(self)
            case 4:
                return self.back()
            case 5:
                self._exit()

    def print_menu(self) -> None:
        print("Menu Commands:")
        print(
            """[1] - Driver Setting\n[2] - Firefox Option\n[3] - Enter\n[4] - Prev Menu\n[5] - Exit"""
        )

    def push(self, data: Any) -> None:
        pass


# TODO fix Chrome menu
class ChromeMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        pass

    def print_menu(self) -> None:
        pass

    def push(self, data: Any) -> None:
        pass


class MainMenu(AbstractMenu):

    def __init__(self):
        super().__init__(self)

    def print_menu(self) -> None:
        print("Select Your Browser:")
        print("""[1] - Firefox\n[2] - Chrome\n[3] - Help\n[4] - Exit""")

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        from .core.abstract import Browsers
        match item_number:
            case 1:
                Driver(Browsers.FireFox)
                return FirefoxMenu(self)
            case 2:
                Driver(Browsers.Chrome)
                return ChromeMenu(self)
            case 3:
                return HelpCommand(self)
            case 4:
                self._exit()  # close the program

    def push(self, data: Any) -> None:
        pass

    def back(self) -> AbstractMenu:
        return self
