from selenium.webdriver.common.by import By

class RegistrationPageLocators:

    FIRSTNAME_INPUT = (By.XPATH, '//input[@name="first_name"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@name="last_name"]')
    USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '(//input[@type="password"])[1]')
    CREATE_ACC_BTN = (By.XPATH, '//button[text()="Создать аккаунт"]')
