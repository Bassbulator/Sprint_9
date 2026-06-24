from pages.base_page import BasePage
from locators.header_locators import HeaderForAuthorizedUser
from locators.header_locators import HeaderForUnauthorizedUser


class HeaderAuth(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderForAuthorizedUser()

    def logout(self):
        self.click(self.locators.LOGOUT_BUTTON)

    def is_logout_btn_visible(self):
        return self.is_element_visible(self.locators.LOGOUT_BUTTON)

    def wait_visible_logout_btn(self):
        self.wait_visible(self.locators.LOGOUT_BUTTON)

    def wait_clickable_create_recipe(self):
        self.wait_clickable(self.locators.CREATE_RECIPE)

    def click_create_recipe(self):
        self.click(self.locators.CREATE_RECIPE)


class HeaderUnauth(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderForUnauthorizedUser()

    def click_create_account_in_header(self):
        self.click(self.locators.CREATE_ACCOUNT_IN_HEADER)

    def wait_clickable_create_account(self):
        self.wait_clickable(self.locators.CREATE_ACCOUNT_IN_HEADER)

    def click_recipe_header(self):
        self.click(self.locators.RECIPE_HEADER_BUTTON)

    def click_enter_in_header(self):
        self.click(self.locators.ENTER_IN_HEADER_BUTTON)