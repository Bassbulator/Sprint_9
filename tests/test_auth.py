import allure

from constants import Url
from pages.auth_page import AuthPage
from pages.header_page import HeaderAuth


class TestAuthUser:

    @allure.title("Вход в систему под учётными данными пользователя")
    def test_auth_user(self, driver, logout_after_test):

        header_auth_page = HeaderAuth(driver)
        auth_page = AuthPage(driver)

        with allure.step("Перейти на страницу входа в аккаунт"):
            auth_page.open_auth_page()

        with allure.step("Выполнить вход с заданными учётными данными"):
            auth_page.login_with_static_data()

        with allure.step("Убедиться, что кнопка выхода стала видимой"):
            header_auth_page.wait_visible_logout_btn()

        with allure.step("Считать адрес текущей страницы"):
            current_url = auth_page.get_current_url()

        with allure.step("Проверить совпадение URL с адресом главной страницы"):
            assert current_url == Url.RECIPES_URL

        with allure.step("Проверить наличие кнопки выхода из аккаунта"):
            assert header_auth_page.is_logout_btn_visible() is True
