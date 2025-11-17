from selenium.webdriver.common.by import By

class BasePageLocators:

    CREATE_ACC_BTN = (By.XPATH, './/a[text()="Создать аккаунт"]')
    LOGIN_BTN = (By.XPATH, './/a[text()="Войти"]')
    LOGOUT_BTN = (By.XPATH, '//a[text()="Выход"]')
    