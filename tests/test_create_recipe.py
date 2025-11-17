
import allure
from datetime import datetime
from configs.urls import Urls
from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.recipe_create_page import RecipeCreatePage
from pages.recipes_page import RecipesPage
from locators.base_page_locators import BasePageLocators


@allure.title("Создание рецепта с загрузкой изображения и проверкой карточки на списке")
def test_create_recipe_with_image(driver, user):
    base_page = BasePage(driver)
    base_page.click_on_element(BasePageLocators.CREATE_ACC_BTN)

    reg_page = RegistrationPage(driver)
    reg_page.register_user(user)

    login_page = LoginPage(driver)
    assert login_page.wait_for_login_form() is True
    login_page.login(username=user["username"], password=user["psw"])
    
    base_page.wait_visibility_of_element(BasePageLocators.LOGOUT_BTN)

    base_page.open_url(Urls.RECIPE_CREATE_PAGE)

    creator = RecipeCreatePage(driver)
    # assert creator.wait_for_recipe_form() is True
    recipe_name = f"Омлет {datetime.utcnow().strftime('%H%M%S')}"
    creator.fill_recipe_form(
        name=recipe_name,
        ingredient_name="яйц",
        ingredient_weight="2",
        cooking_time="15",
        description="Простой омлет с яйцами."
    )
    creator.upload_image()
    creator.submit()

    base_page.open_url(Urls.RECIPES_PAGE)
    base_page.check_current_page_url(Urls.RECIPES_PAGE)
    recipes_page = RecipesPage(driver)
    recipes_page.wait_for_recipes_cards(RecipesPageLocators.RECIPES_HEADER)
    assert recipes_page.is_recipe_card_visible(recipe_name) is True
