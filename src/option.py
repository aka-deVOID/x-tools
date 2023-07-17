from selenium.webdriver import FirefoxOptions, ChromeOptions, Proxy
from selenium.webdriver.common.proxy import ProxyType

from abstract import ABC


class Option(ABC):
    def __init__(self, deriver_name: str) -> None:
        self.proxy: Proxy | None = None
        match deriver_name:
            case "firefox":
                self.options = FirefoxOptions()
            case "chrome":
                self.options = ChromeOptions()

    def set_proxy(self, ip: str, port: str) -> None:
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = f"{ip}:{port}"
        self.proxy.ftp_proxy = f"{ip}:{port}"
        self.proxy.socks_proxy = f"{ip}:{port}"
        self.options.proxy = self.proxy
