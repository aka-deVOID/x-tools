from __future__ import annotations
from abc import ABC, abstractmethod

from rich.pretty import pprint


class AbstractMenu(ABC):
    """top-level abstraction for menus"""

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


class Singleton:
    _instance_ = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance_, cls):
            cls._instance = object.__new__(cls, args, kwargs)
        return cls._instance_
