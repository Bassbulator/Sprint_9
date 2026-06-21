from selenium.webdriver.common.by import By


class RegistrationLocators:

    FIRST_NAME_INPUT = [By.XPATH, "//input[@name='first_name']"]

    LAST_NAME_INPUT = [By.XPATH, "//input[@name='last_name']"]

    USERNAME_INPUT = [By.XPATH, "//input[@name='username']"]

    CREATE_BUTTON = [By.XPATH, "//button[contains(text(),'Создать аккаунт')]"]