from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions, FirefoxProfile
from ..exceptions import DriverDoesNotSupported
from .handler import Twitter
from typing import Self
from .abstract import Abstract, Singleton
import platform


class Driver(Abstract, metaclass=Singleton):
    """Driver builder build WebDriver instance."""

    def __init__(self, driver_name: str, options: FirefoxOptions | ChromeOptions = None,
                 profile: FirefoxProfile = None) -> None:
        """
        :raise DriverDoesNotSupported
        """
        self.driver_logger: str | None = None
        self.driver_options: ChromeOptions | FirefoxOptions | None = options
        self.driver_keep_alive: bool = False
        self.platform: str = platform.system()
        match driver_name:
            case "chrome":
                self.driver = Chrome
            case "firefox":
                self.profile: FirefoxProfile = profile
                self.driver = Firefox
            case _:
                raise DriverDoesNotSupported(f"{driver_name} does not supported.")

    def keep_alive(self, toggle: bool = False) -> Self:
        self.driver_keep_alive = toggle
        return self

    def log_system(self, toggle: bool = True) -> Self:
        """TODO: fix here not working test on windows."""
        if not toggle:
            if self.platform == "Windows":
                self.driver_logger = "NULL"
            else:
                self.driver_logger = "/dev/null"
        else:
            self.driver_logger = None

        return self

    def build(self) -> Twitter:
        """
            TODO: move option to driver
        """
        if self.driver_logger:
            driver = self.driver(options=self.driver_options, keep_alive=self.driver_keep_alive,
                                 service_log_path=self.driver_logger)  # TODO: fix service_log_path not working
        else:
            driver = self.driver(options=self.driver_options, keep_alive=self.driver_keep_alive)
            return Twitter(driver)
