from __future__ import annotations
import sys
from .abstracts import AbstractMenu, AbstractCommand
from .commands import HelpCommand  # cause cycle error


class FirefoxDriverMenu(AbstractMenu):
    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                pass
            case 2:
                pass
            case 3:
                return self.back()
            case 4:
                return self.back()

    def print_menu(self) -> None:
        print("Select your option:")
        print("""[1] - Keep Alive (default Disable)
[2] - Browser Logging (default Disable)
[3] - Enter (Save Settings)
[4] - Perv Menu (Settings are dropped)
        """)

    def back(self) -> AbstractMenu:
        return FirefoxMenu()


class FirefoxOptionMenu:
    pass


class FirefoxProfileMenu:
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
                return FirefoxMenu()

    def print_menu(self) -> None:
        print("Select One Option:")
        print(
            "[1] - Delete Tweets (+Medias)\n[2] - Delete Medias\n[3] - Delete Replies\n[4] - Remove Likes\n[5] - Remove Followings\n[6] - Prev Menu"
        )

    def back(self) -> AbstractMenu:
        pass


class FirefoxMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                return FirefoxDriverMenu()
            case 2:
                return FirefoxOptionMenu()
            case 3:
                return FirefoxProfileMenu()
            case 4:
                return ToolsMenu()
            case 5:
                return self.back()

    def print_menu(self) -> None:
        print("Menu Commands:")
        print(
            """[1] - Driver Setting\n[2] - Firefox Option\n[3] - Firefox Profile\n[4] - Enter\n[5] - Prev Menu"""
        )

    def back(self) -> AbstractMenu:
        return MainMenu()


class ChromeMenu(AbstractMenu):

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        pass

    def print_menu(self) -> None:
        pass

    def back(self) -> AbstractMenu:
        pass


class MainMenu(AbstractMenu):
    def print_menu(self) -> None:
        print("Select Your Browser:")
        print("""[1] - Firefox\n[2] - Chrome\n[3] - Help\n[4] - Exit""")

    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        match item_number:
            case 1:
                return FirefoxMenu()
            case 2:
                return ChromeMenu()
            case 3:
                return HelpCommand(self)
            case 4:
                sys.exit()  # close the program

    def back(self) -> MainMenu:
        raise NotImplemented
