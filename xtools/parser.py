from .menus import MainMenu


def initialize_cmd():  # TODO fix
    logo = r''' ______         _  __   __              ______            __
/_  __/_    __ (_)/ /_ / /_ ___  ____  /_  __/___  ___   / /___
 / /  | |/|/ // // __// __// -_)/ __/   / /  / _ \/ _ \ / /(_-<
/_/   |__,__//_/ \__/ \__/ \__//_/     /_/   \___/\___//_//___/'''
    description = r'''
----------------------------------------------------------------------
Twitter Tools made it for remove your tweets and following and more ...
You can Delete Tweets, Delete Replies, Remove Likes, Remove Followings and Delete Medias ...

---- ~ ----
- Repository: https://github.com/aka-deVOID/twitter-tools
- Support: Soon
    '''

    print(logo)
    print(description)


class MainLoop:
    def __init__(self):
        initialize_cmd()
        self.loop()

    def loop(self):
        current_menu = MainMenu().exec()
        while True:
            current_menu = current_menu.exec()


def execute() -> None:
    MainLoop()
