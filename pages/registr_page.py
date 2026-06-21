from constants import Url
from helpers import GenDataForUser
from pages.base_page import BasePage
from locators.auth_locators import AuthLocators
from locators.registr_locators import RegistrationLocators


class RegistrPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.reg_locators = RegistrationLocators()
        self.auth_locators = AuthLocators()

    def get_registration_page(self):
        self.open_page(Url.AUTH_URL)

    def wait_clickable_username_input(self):
        self.wait_clickable(self.reg_locators.USERNAME_INPUT)

    def enter_registration_form(self):
        first_name = GenDataForUser.generate_first_name()
        last_name = GenDataForUser.generate_last_name()
        username = GenDataForUser.generate_username()
        email = GenDataForUser.generate_email()
        password = GenDataForUser.generate_password()
        self.send_keys(self.reg_locators.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.reg_locators.LAST_NAME_INPUT, last_name)
        self.send_keys(self.reg_locators.USERNAME_INPUT, username)
        self.send_keys(self.auth_locators.EMAIL_INPUT, email)
        self.send_keys(self.auth_locators.PASSWORD_INPUT, password)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password,
        }

    def click_create_account(self):
        self.click(self.reg_locators.CREATE_BUTTON)

    def wait_url_to_be_auth(self):
        self.wait_url_to_be(Url.AUTH_URL)
