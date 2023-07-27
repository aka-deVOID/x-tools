from typing import Self

from selenium.webdriver import FirefoxOptions, ChromeOptions, Proxy
from selenium.webdriver.common.proxy import ProxyType
from abstract import Abstract, Singleton


class Option(Abstract, metaclass=Singleton):
    def __init__(self, deriver_name: str) -> None:
        self.proxy: Proxy | None = None
        match deriver_name:
            case "firefox":
                self.options = FirefoxOptions()
            case "chrome":
                self.options = ChromeOptions()
            case _:
                from ..exceptions import BrowserNameIsNotValid
                raise BrowserNameIsNotValid(f"{deriver_name} ")

    def set_proxy(self, ip: str, port: str) -> Self:
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = f"{ip}:{port}"
        # self.proxy.ftp_proxy = f"{ip}:{port}"
        self.proxy.socks_proxy = f"{ip}:{port}"
        # self.proxy.ssl_proxy = f"{ip}:{port}"
        self.proxy.socks_version = 5
        self.options.proxy = self.proxy
        return self

    def __enable_mobile(self):
        """For now we don't support android"""
        ...

    def to_capabilities(self):
        ...

    def binary_location(self):
        ...

    def default_capabilities(self):
        ...

    def headless(self, toggle: bool = False):
        self.options.headless = toggle

    def preferences(self):
        ...

    def profile(self):
        ...

    def build(self) -> FirefoxOptions | ChromeOptions:
        return self.options
