from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .abstract import Abstract
from selenium.common.exceptions import TimeoutException


class X(Abstract):

    def __init__(self, driver: Firefox | Chrome) -> None:
        self.driver = driver

    def load_time_out(self, second: int = 60) -> None:
        self.driver.set_page_load_timeout(second)

    def run(self) -> None:
        try:
            self.driver.get("https://twitter.com/")
            self.log("info", "Request sended.")
        except TimeoutException:
            self.log("error", "Twitter not loaded, check internet connection or proxy setting")
            self.driver.quit()
        else:
            self.log("info", "Twitter Loaded Succesfully.")
