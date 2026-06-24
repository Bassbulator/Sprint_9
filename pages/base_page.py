from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, locator):
        for attempt in range(3):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
                continue

    def wait_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    def send_keys(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_visible(self, locator, timeout=10):
        self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator, timeout=10):
        timeout = timeout or 10
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def get_ingredient_counter(self, locator):
        counter = self.find_element(locator)
        return int(counter.text)

    def get_order_id(self, locator):
        order_id = self.find_element(locator)
        return int(order_id.text)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_present(self, locator, timeout=5):
        try:
            self.find_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator, timeout=5):
        try:
            self.wait_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def send_keys_to_hidden_element(self, locator, value):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(value)

    def click_with_retry(self, locator, max_attempts=3):
        for attempt in range(max_attempts):
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
                return
            except StaleElementReferenceException:
                if attempt == max_attempts - 1:
                    raise
                continue
