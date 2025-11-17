from selenium.webdriver.common.by import By


class RecipeCreatePageLocators:

    RECIPE_NAME_INPUT = (By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input')
    BREACKFAST_CHECKBOX = (By.XPATH, '//button[@type="button" and contains(@style, "orange")]')
    INGREDIENT_NAME_INPUT = (By.XPATH, '//form/div[contains(., "Ингредиенты")]//following-sibling::input')
    INGREDIENT_WEIGHT_INPUT = (By.XPATH, '//div[text()="Добавить ингредиент"]//preceding::input[1]')
    INGREDIENTS_LIST = (By.XPATH, '//ya-tr-span[@data-value="Добавить ингредиент"]//preceding::div[4]')
    INGREDIENT_SELECTOR_FROM_LIST = (By.XPATH, '//div[text()="яйца куриные"]')
    ADD_INGREDIENT_BTN = (By.XPATH, '//div[text()="Добавить ингредиент"]')
    COOKING_TIME_INPUT = (By.XPATH, '//div[text()="Время приготовления"]//following-sibling::input')
    DESCRIPTION_INPUT = (By.XPATH, '//div[text()="Описание рецепта"]//following-sibling::textarea')
    FILE_INPUT = (By.XPATH, "//input[@type='file']")
    FILE_SELECTION_BTN = (By.XPATH, './/button[text()="Выбрать файл"]')
    CREATE_RECIPE_BTN = (By.XPATH, './/button[text()="Создать рецепт"]')
