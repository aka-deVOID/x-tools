from time import sleep

from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .abstract import Abstract
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class X(Abstract):
    def __init__(self, driver) -> None:
        self.driver = driver

    def load_time_out(self, second: int = 60) -> None:
        self.driver.set_page_load_timeout(second)

    def run(self) -> None:
        try:
            self.driver.get("https://twitter.com/")
            self.log("info", "Request sended.")
        except TimeoutException:
            self.log(
                "error",
                "Twitter not loaded, check internet connection or proxy setting",
            )
            self.driver.quit()
        else:
            self.log("info", "Twitter Loaded Succesfully.")

    def login(self):
        alias = self.driver
        login_button = alias.find_element(
            By.CSS_SELECTOR, "a.css-1dbjc4n:nth-child(2) > div:nth-child(1)"
        )
        login_button.click()
        sleep(10)
        # Wait here
        # Check Login Box
        try:
            alias.find_element(By.CSS_SELECTOR, ".r-1867qdf")
        except NoSuchElementException:
            pass
        sleep(10)
        inp_mail = input("mail: ").strip()
        # TODO: check regex email
        login_popup = alias.find_element(By.CSS_SELECTOR, ".r-30o5oe")
        login_popup.send_keys(inp_mail)  # Send Gmail

        login_popup_next_button = alias.find_element(
            By.CSS_SELECTOR, "div.css-18t94o4:nth-child(6) > div:nth-child(1)"
        )
        login_popup_next_button.click()
        sleep(10)

        password_input = alias.find_element(By.CSS_SELECTOR, ".r-homxoj")
        inp_passwd = input("password: ").strip()
        password_input.send_keys(inp_passwd)

        login_btn = alias.find_element(By.CSS_SELECTOR, ".r-19yznuf > div:nth-child(1)")
        login_btn.click()
        # check box updated
        try:
            user_cell = alias.find_element(By.CSS_SELECTOR, "li.css-4rbku5")
        except NoSuchElementException:
            pass

        confirm_code = alias.find_element(By.CSS_SELECTOR, ".r-30o5oe")
        inp_code = input("code: ")
        confirm_code.send_keys(inp_code)
        check_email_next_button = alias.find_element(
            By.CSS_SELECTOR, ".r-19yznuf > div:nth-child(1)"
        )
        check_email_next_button.click()
        if alias.current_url == "https://twitter.com" or "https://x.com":
            return "OK"
        else:
            return "Err"

    def to_profile(self):
        alias = self.driver
        profile = alias.find_element(
            By.CSS_SELECTOR, "a.css-4rbku5:nth-child(7) > div:nth-child(1)"
        )
        profile.click()
        try:
            alias.find_element(By.CSS_SELECTOR, "a.r-6gpygo")
        except NoSuchElementException:
            pass
