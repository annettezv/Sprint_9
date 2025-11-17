import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class RecipesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Дождаться видимости карточек рецептов")
    def wait_for_recipes_cards(self, locator, timeout: int =10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Проверить, что созданная карточка рецепта есть на странице")
    def is_recipe_card_visible(self, name: str) -> bool:
        xpath = (
            f"//a[normalize-space()='{name}'] | "
            f"//h3[normalize-space()='{name}'] | "
            f"//div[contains(@class,'card')]//*[self::h3 or self::a][normalize-space()='{name}']"
        )
        elements = self.driver.find_elements(By.XPATH, xpath)
        return len(elements) > 0
