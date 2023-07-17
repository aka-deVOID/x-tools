from selenium.webdriver import Chrome, Firefox, Edge
from src.exceptions import DriverDoesNotSupported


class Driver:
    def __init__(self, driver_name: str) -> None:
        match driver_name:
            case "chrome":
                self.driver = Chrome
            case "firefox":
                self.driver = Firefox
            case "safari":
                self.driver = Edge
            case _:
                raise DriverDoesNotSupported(f"{driver_name} does not supported.")

    def options(self) -> None:
        """
            TODO: Add WebDriver Options
        """
        self.driver_options = ...
        pass

    def build(self) -> Chrome | Firefox | Edge:
        """
            TODO: move option to driver
        """
        return self.driver()
