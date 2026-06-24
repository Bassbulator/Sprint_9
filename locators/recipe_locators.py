from selenium.webdriver.common.by import By


class RecipeLocators:

    RECIPE_NAME_INPUT = [By.XPATH, "//*[contains(text(), 'Название рецепта')]/ancestor::label//input"]

    INGREDIENTS_INPUT = [By.XPATH, "//*[contains(text(), 'Ингредиенты')]/ancestor::label//input"]

    FIRST_INGREDIENT = [By.CSS_SELECTOR, "div.styles_container__3ukwm > div:first-child"]

    ADD_INGREDIENTS = [By.XPATH, "//div[contains(text(),'Добавить ингредиент')]"]

    GRAMS_INPUT = [By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT"]

    COOKING_TIME = [By.XPATH, "//*[contains(text(), 'Время приготовления')]/ancestor::label//input"]

    DESCRIPTION_RECIPE = [By.XPATH, "//*[contains(text(), 'Описание рецепта')]/ancestor::label//textarea",]

    SELECT_FILE = [By.CSS_SELECTOR, "input[type='file']"]

    CREATE_RECIPE_BUTTON = [By.XPATH, "//button[contains(text(), 'Создать рецепт')]"]

    RECIPE_CARD = [By.CSS_SELECTOR, "div.styles_single-card__info__2_cny"]

    RECIPE_NAME = [By.XPATH, "//h1"]