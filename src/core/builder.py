from abstract import Abstract
from option import Option


class Builder(Abstract):
    """
        factory builder to create options, profile and move them to build Driver
    """

    def __init__(self):
        ...

    def options(self):
        ...

    def profile(self):
        ...

    def build(self):
        ...
