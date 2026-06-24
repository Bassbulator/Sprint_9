from selenium.webdriver.common.by import By


class HeaderForUnauthorizedUser:

    CREATE_ACCOUNT_IN_HEADER = [By.XPATH, "//a[contains(text(), 'Создать аккаунт')]"]

    ENTER_IN_HEADER_BUTTON = [By.XPATH, "//header//a[contains(text(), 'Войти')]"]

    RECIPE_HEADER_BUTTON = [By.XPATH, "//header//a[contains(text(), 'Рецепты')]"]


class HeaderForAuthorizedUser:

    CREATE_RECIPE = [By.XPATH, "//a[contains(text(), 'Создать рецепт')]"]

    LOGOUT_BUTTON = [By.XPATH, "//a[contains(text(), 'Выход')]"]