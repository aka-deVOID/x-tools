from .menus import MainMenu
from .abstracts import ErrorHandler


def initialize_cmd():  # TODO fix
    logo = r"""
   _  __    ______            __
  | |/ /   /_  __/___  ____  / /____
  |   /     / / / __ \/ __ \/ / ___/
 /   |     / / / /_/ / /_/ / (__  )
/_/|_|    /_/  \____/\____/_/____/"""
    description = r"""
----------------------------------------------------------------------
X Tools made it for remove your tweets and following and more ...
You can Delete Tweets, Delete Replies, Remove Likes, Remove Followings and Delete Medias ...

---- ~ ----
- Repository: https://github.com/aka-deVOID/x-tools
- Support: Soon
    """

    print(logo)
    print(description)


class MainLoop(ErrorHandler):
    def __init__(self):
        initialize_cmd()
        self.loop()

    def loop(self):
        current_menu = MainMenu().exec()
        while True:
            current_menu = current_menu.exec()


def execute() -> None:
    MainLoop()
