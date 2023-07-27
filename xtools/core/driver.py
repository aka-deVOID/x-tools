from __future__ import annotations
from selenium.webdriver import Chrome, Firefox, ChromeOptions, FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from .handler import X
from .abstract import Abstract, Singleton, Browsers


class Driver(Abstract, metaclass=Singleton):
    """Driver builder build WebDriver instance."""

    def __init__(self, browser: Browsers = None) -> None:
        """
        :raise DriverDoesNotSupported
        """
        self.__driver_options: ChromeOptions | FirefoxOptions | None = None
        self.__driver_keep_alive: bool = False
        self.__driver_service = None
        match browser:
            case Browsers.Chrome:
                self.__driver = Chrome
            case Browsers.FireFox:
                self.__driver = Firefox
            case _:
                from ..exceptions import DriverDoesNotSupported
                raise DriverDoesNotSupported(f"{browser} does not supported.")

    @property
    def service(self) -> FirefoxService | ChromeService:
        return self.__driver_service

    @service.setter
    def service(self, service: FirefoxService | ChromeService):
        if isinstance(service, FirefoxService) and isinstance(self.__driver, Firefox):
            self.__driver_service = service
        elif isinstance(service, ChromeService) and isinstance(self.__driver, Chrome):
            self.__driver_service = service
        else:
            from ..exceptions import OptionIsNotValid
            raise OptionIsNotValid("service type is not same with driver")

    @property
    def options(self) -> ChromeOptions | FirefoxOptions:
        return self.__driver_options

    @options.setter
    def options(self, options: ChromeOptions | FirefoxOptions) -> None:
        if isinstance(options, FirefoxOptions) and isinstance(self.__driver, Firefox):
            self.__driver_options = options
        elif isinstance(options, ChromeOptions) and isinstance(self.__driver, Chrome):
            self.__driver_options = options
        else:
            from ..exceptions import OptionIsNotValid
            raise OptionIsNotValid("option type is not same with driver")

    @property
    def keep_alive(self) -> bool:
        return self.__driver_keep_alive

    @keep_alive.setter
    def keep_alive(self, toggle: bool = False) -> None:
        self.__driver_keep_alive = toggle

    def build(self) -> X:
        return X(self.__driver(options=self.__driver_options,
                               keep_alive=self.__driver_keep_alive))
