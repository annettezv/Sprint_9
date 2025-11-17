import allure
from pathlib import Path
from pages.base_page import BasePage
from locators.recipe_create_page_locators import RecipeCreatePageLocators


class RecipeCreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RecipeCreatePageLocators()
        self.app_dir = Path(__file__).resolve().parents[1]

    @allure.step("Заполнить форму создания рецепта")
    def fill_recipe_form(self, name: str, ingredient_name: str, ingredient_weight: str, cooking_time: str, description: str):
        self.fill_input(self.locators.RECIPE_NAME_INPUT, name)
        try:
            self.click_on_element(self.locators.BREACKFAST_CHECKBOX)
        except Exception:
            pass
        self.fill_input(self.locators.INGREDIENT_NAME_INPUT, ingredient_name)
        self.fill_input(self.locators.INGREDIENT_NAME_INPUT, ingredient_name)
        self.click_on_element(self.locators.INGREDIENT_SELECTOR_FROM_LIST)
        self.fill_input(self.locators.INGREDIENT_WEIGHT_INPUT, ingredient_weight)
        self.click_on_element(self.locators.ADD_INGREDIENT_BTN)
        self.fill_input(self.locators.COOKING_TIME_INPUT, cooking_time)
        self.fill_input(self.locators.DESCRIPTION_INPUT, description)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, file_name: str = "e1a75335-ee1f-4b7c-8d81-7cdffc98c3d2.jpg"):
        image_path = self.app_dir / "assets" / file_name
        input_el = self.find_element(self.locators.FILE_INPUT)
        input_el.send_keys(str(image_path))

    @allure.step("Создать рецепт")
    def submit(self):
        self.click_on_element(self.locators.CREATE_RECIPE_BTN)
