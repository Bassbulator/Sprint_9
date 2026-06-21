from selenium.webdriver.common.by import By


class AuthLocators:
    
    LOGIN_BUTTON = [By.XPATH, "//button[contains(text(),'Войти')]"]
    EMAIL_INPUT = [By.XPATH, "//input[@name='email']"]
    PASSWORD_INPUT = [By.XPATH, "//input[@name='password']"]