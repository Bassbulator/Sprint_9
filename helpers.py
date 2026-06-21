import os
import random
import string
from faker import Faker
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name: str, headless: bool = False):
        selenoid_url = os.environ.get("SELENOID_URL")

        if selenoid_url:
            options = ChromeOptions()
            options.add_argument("--disable-save-password-bubble")
            options.add_experimental_option(
                "prefs",
                {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False,
                },
            )
            return RemoteWebDriver(command_executor=selenoid_url, options=options)
        else:
            if browser_name.lower() == "chrome":
                options = ChromeOptions()
                if headless:
                    options.add_argument("--headless")
                options.add_argument("--disable-save-password-bubble")
                options.add_experimental_option(
                    "prefs",
                    {
                        "credentials_enable_service": False,
                        "profile.password_manager_enabled": False,
                    },
                )
                return webdriver.Chrome(options=options)


class GenDataForUser:

    fake = Faker()

    @staticmethod
    def generate_first_name():
        first_name = GenDataForUser.fake.first_name()
        return first_name

    @staticmethod
    def generate_last_name():
        last_name = GenDataForUser.fake.last_name()
        return last_name

    @staticmethod
    def generate_email():
        email = GenDataForUser.fake.email()
        return email

    @staticmethod
    def generate_password():
        return f"Test{GenDataForUser.generate_random_string(8)}3!"

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generate_username():
        username = f"test{GenDataForUser.generate_random_string(8)}"
        return username


class DataForRecipe:

    @staticmethod
    def generate_recipe_name():
        return f"Recipe_{GenDataForUser.generate_random_string(8)}"

    @staticmethod
    def generate_ingredient_name():
        ingredients = ["Tomato", "Cheese", "Onion", "Garlic", "Salt", "Pepper"]
        return random.choice(ingredients)

    @staticmethod
    def generate_grams():
        return str(random.randint(50, 500))

    @staticmethod
    def generate_cooking_time():
        return str(random.randint(10, 180))

    @staticmethod
    def generate_description():
        return f"Delicious recipe made with love. {GenDataForUser.generate_random_string(30)}"

    @staticmethod
    def get_file_path(filename):
        app_dir = Path(__file__).parent
        return str(app_dir / "assets" / filename)

    @staticmethod
    def get_generated_recipe_data():
        return {
            "name": f"Recipe_{GenDataForUser.generate_random_string(8)}",
            "cooking_time": str(random.randint(10, 180)),
            "description": f"Delicious recipe {GenDataForUser.generate_random_string(20)}",
            "image_filename": "recipe.jpg",
        }
