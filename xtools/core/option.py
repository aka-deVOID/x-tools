import ipaddress
from typing import Self
from selenium.webdriver import FirefoxOptions, ChromeOptions, Proxy
from selenium.webdriver.common.proxy import ProxyType
from .abstract import Abstract, Singleton, Browsers


class Option(Abstract, metaclass=Singleton):
    def __init__(self, browser: Browsers = None) -> None:
        self.proxy: Proxy | None = None
        match browser:
            case Browsers.FireFox:
                alias = self.__options = FirefoxOptions()
            case Browsers.Chrome:
                alias = self.__options = ChromeOptions()
            case _:
                from ..exceptions import BrowserNameIsNotValid
                raise BrowserNameIsNotValid(f"{browser} ")
        alias.platform_name = "X Tools"

    def set_proxy(self, ip: str, port: int) -> Self:
        alias = self.__options
        ip = ip.strip()
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            from ..exceptions import IPIsNotValid
            raise IPIsNotValid(f"{ip!r} ip is not valid")
        else:
            ip = ip + ":" + str(port)
            alias.proxy = Proxy()
            alias.proxy.proxyType = ProxyType.MANUAL
            alias.proxy.httpProxy = alias.proxy.socksProxy = ip
        return self

    def build(self) -> FirefoxOptions | ChromeOptions:
        return self.__options
