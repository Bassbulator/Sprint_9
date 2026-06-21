from helpers import DataForRecipe


class RecipeData:

    @staticmethod
    def get_ingredients():
        # Статичные ингредиенты или тоже можно генерировать
        return [{"name": "картофель", "grams": 200}, {"name": "сайра", "grams": 150}]

    @staticmethod
    def get_recipe_name():
        return DataForRecipe.generate_recipe_name()

    @staticmethod
    def get_cooking_time():
        return DataForRecipe.generate_cooking_time()

    @staticmethod
    def get_description():
        return DataForRecipe.generate_description()


class TestUser:

    EMAIL = "Test_login_page@yandex.ru"
    PASSWORD = "test12345678"
    USERNAME = "testTestovich"