from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    LINK = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def navigate_to_login_page(self):
        self.driver.get(self.LINK)

    def set_correct_username_and_password(self):
        self.type(self.USERNAME, "standard_user")
        self.type(self.PASSWORD, "secret_sauce")

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def verify_url(self):
        assert self.LINK != self.driver.current_url












