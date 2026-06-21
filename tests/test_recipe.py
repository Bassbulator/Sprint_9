import allure

from test_data import RecipeData
from pages.auth_page import AuthPage
from pages.header_page import HeaderAuth
from pages.recipe_page import RecipePage


class TestCreatingRecipe:

    @allure.title("Публикация нового рецепта от имени авторизованного пользователя")
    @allure.description("Проверяет полный цикл добавления рецепта: заполнение формы, загрузку фото и подтверждение создания")
    def test_create_recipe(self, driver, logout_after_test):

        auth_page = AuthPage(driver)
        recipe_page = RecipePage(driver)
        header_page = HeaderAuth(driver)

        with allure.step("Перейти на страницу входа в аккаунт"):
            auth_page.open_auth_page()

        with allure.step("Выполнить вход с заранее подготовленными данными"):
            auth_page.login_with_static_data()

        with allure.step("Ожидать активности кнопки перехода к форме рецепта"):
            header_page.wait_clickable_create_recipe()

        with allure.step("Открыть форму создания нового рецепта"):
            header_page.click_create_recipe()

        with allure.step("Ожидать готовности формы рецепта к вводу"):
            recipe_page.wait_clickable_name_recipe()

        with allure.step("Заполнить поле с наименованием блюда"):
            recipe_name = RecipeData.get_recipe_name()
            recipe_page.fill_recipe_name(recipe_name)

        with allure.step("Внести значение времени готовки"):
            cooking_time = RecipeData.get_cooking_time()
            recipe_page.fill_cooking_time(cooking_time)

        with allure.step("Добавить текстовое описание блюда"):
            description = RecipeData.get_description()
            recipe_page.fill_description(description)

        with allure.step("Прикрепить изображение готового блюда"):
            recipe_page.upload_image("recipe.jpg")

        ingredients = RecipeData.get_ingredients()

        with allure.step(f"Указать ингредиент '{ingredients[0]['name']}' — {ingredients[0]['grams']} г"):
            recipe_page.fill_ingredients(ingredients[0]["name"])
            recipe_page.fill_grams(str(ingredients[0]["grams"]))
            recipe_page.click_add_ingredient()

        with allure.step(f"Указать ингредиент '{ingredients[1]['name']}' — {ingredients[1]['grams']} г"):
            recipe_page.fill_ingredients(ingredients[1]["name"])
            recipe_page.fill_grams(str(ingredients[1]["grams"]))
            recipe_page.click_add_ingredient()

        with allure.step("Отправить форму на сохранение рецепта"):
            recipe_page.click_create_recipe_button()

        with allure.step("Ожидать загрузки страницы с карточкой рецепта"):
            recipe_page.wait_visible_recipe_card()

        with allure.step("Считать название рецепта с открывшейся карточки"):
            name_from_card = recipe_page.get_recipe_name_from_card()

        with allure.step("Убедиться, что карточка рецепта присутствует на странице"):
            assert recipe_page.is_recipe_card_displayed()

        with allure.step("Убедиться, что имя рецепта на карточке совпадает с введённым"):
            assert name_from_card == recipe_name
