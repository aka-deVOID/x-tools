from .abstract import Abstract, Singleton


class Profile(Abstract, metaclass=Singleton):
    ...
