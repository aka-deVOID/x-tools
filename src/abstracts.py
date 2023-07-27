from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from rich.pretty import pprint


class AbstractMenu(ABC):
    """top-level abstraction for menus"""

    @abstractmethod
    def __init__(self, perv_menu: AbstractMenu = None) -> None:
        self.perv_menu = perv_menu

    @abstractmethod
    def print_menu(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def select_item(self, item_number: int) -> AbstractCommand | AbstractMenu:
        raise NotImplementedError

    @abstractmethod
    def back(self) -> AbstractMenu:
        raise NotImplementedError

    # TODO: def menu_builder(self, *args: list[str]): ...

    @abstractmethod
    def push(self, data: Any) -> None:
        """ push data from menu or command """
        raise NotImplementedError

    def exec(self) -> AbstractMenu:
        self.print_menu()
        while True:
            try:
                item = int(input("enterr item number: "))
            except ValueError:
                pprint("wrong input type.")
                continue
            else:
                return self.select_item(item)


class AbstractCommand(ABC):
    """top-level abstraction for commands"""

    def __init__(self, menu: AbstractMenu):
        self.menu = menu

    @abstractmethod
    def exec(self) -> AbstractMenu: raise NotImplementedError
