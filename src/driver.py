from selenium.webdriver import Chrome, Firefox
from src.exceptions import DriverDoesNotSupported


class Driver:
    def __init__(self, driver_name: str) -> None:
        self.driver_options = None
        self.driver_keep_alive = False
        match driver_name:
            case "chrome":
                self.driver = Chrome
            case "firefox":
                self.driver = Firefox
            case _:
                raise DriverDoesNotSupported(f"{driver_name} does not supported.")

    def options(self) -> None:
        """
            TODO: Add WebDriver Options
        """
        pass

    def keep_alive(self, toggle: bool = False):
        self.driver_keep_alive = toggle

    def build(self) -> Chrome | Firefox:
        """
            TODO: move option to driver
        """
        return self.driver(keep_alive=self.driver_keep_alive)
