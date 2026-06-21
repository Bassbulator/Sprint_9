import allure

from constants import Url
from pages.auth_page import AuthPage
from pages.registr_page import RegistrPage
from pages.header_page import HeaderUnauth


class TestRegistrUser:

    @allure.title("Создание нового аккаунта в системе")
    @allure.description("Проверяет, что после заполнения формы регистрации пользователь перенаправляется на страницу входа")
    def test_registr_user(self, driver):

        reg_page = RegistrPage(driver)

        with allure.step("Перейти на стартовую страницу приложения"):
            reg_page.get_registration_page()

        header_page = HeaderUnauth(driver)

        with allure.step("Ожидать активности ссылки регистрации в шапке"):
            header_page.wait_clickable_create_account()

        with allure.step("Перейти на страницу регистрации через шапку сайта"):
            header_page.click_create_account_in_header()

        with allure.step("Ожидать готовности формы регистрации к вводу данных"):
            reg_page.wait_clickable_username_input()

        with allure.step("Внести данные нового пользователя в форму"):
            reg_page.enter_registration_form()

        with allure.step("Подтвердить создание аккаунта, нажав кнопку отправки"):
            reg_page.click_create_account()

        with allure.step("Ожидать автоматического перехода на страницу входа"):
            reg_page.wait_url_to_be_auth()

        with allure.step("Считать адрес страницы после регистрации"):
            current_url = reg_page.get_current_url()

            auth_page = AuthPage(driver)

        with allure.step("Проверить, что URL соответствует странице входа"):
            assert current_url == Url.AUTH_URL

        with allure.step("Проверить видимость формы входа в аккаунт"):
            assert auth_page.is_enter_visible() is True
