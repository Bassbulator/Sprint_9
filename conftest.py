import pytest

from pages.header_page import HeaderAuth
from helpers import BrowserFactory


@pytest.fixture(params=["chrome"])
def driver(request):

    driver = BrowserFactory.get_driver(request.param, headless=False)
    driver.delete_all_cookies()
    yield driver
    driver.quit()


@pytest.fixture
def logout_after_test(driver):
    yield
    try:
        header_auth = HeaderAuth(driver)
        header_auth.logout()
    except Exception:
        pass