from pathlib import Path
from pages.base_page import BasePage
from locators.recipe_locators import RecipeLocators


class RecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipeLocators()

    def fill_recipe_name(self, name):
        self.send_keys(self.locators.RECIPE_NAME_INPUT, name)

    def fill_ingredients(self, ingredient_name):
        self.send_keys(self.locators.INGREDIENTS_INPUT, ingredient_name)
        self.click_with_retry(self.locators.FIRST_INGREDIENT)

    def click_add_ingredient(self):
        self.click(self.locators.ADD_INGREDIENTS)

    def fill_grams(self, grams):
        self.send_keys(self.locators.GRAMS_INPUT, grams)

    def fill_cooking_time(self, minutes):
        self.send_keys(self.locators.COOKING_TIME, minutes)

    def fill_description(self, description):
        self.send_keys(self.locators.DESCRIPTION_RECIPE, description)

    def upload_image(self, filename):
        app_dir = Path(__file__).parent.parent
        file_path = str(app_dir / "assets" / filename)
        self.send_keys_to_hidden_element(self.locators.SELECT_FILE, file_path)

    def click_create_recipe_button(self):
        self.click(self.locators.CREATE_RECIPE_BUTTON)

    def is_recipe_card_displayed(self):
        return self.is_element_visible(self.locators.RECIPE_CARD)

    def get_recipe_name_from_card(self):
        return self.get_text(self.locators.RECIPE_NAME)

    def wait_visible_recipe_card(self):
        self.wait_visible(self.locators.RECIPE_CARD)

    def wait_clickable_name_recipe(self):
        self.wait_clickable(self.locators.RECIPE_NAME)

    def wait_clickable_create_recipe_btn(self):
        self.wait_clickable(self.locators.CREATE_RECIPE_BUTTON)