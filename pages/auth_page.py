from constants import Url
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
from test_data import TestUser


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AuthLocators()

    def open_auth_page(self):
        self.open_page(Url.AUTH_URL)

    def is_enter_visible(self):
        return self.is_element_visible(self.locators.LOGIN_BUTTON)

    def click_enter_button(self):
        self.click(self.locators.LOGIN_BUTTON)

    def login_with_static_data(self):
        self.send_keys(self.locators.EMAIL_INPUT, TestUser.EMAIL)
        self.send_keys(self.locators.PASSWORD_INPUT, TestUser.PASSWORD)

        self.click(self.locators.LOGIN_BUTTON)
        self.wait_url_to_be(Url.RECIPES_URL)