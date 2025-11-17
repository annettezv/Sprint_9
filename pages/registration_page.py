import allure

from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RegistrationPageLocators()

    @allure.step("Заполнить форму регистрации")
    def fill_registration_form(self, user: dict):
        self.fill_input(self.locators.FIRSTNAME_INPUT, user['firstname'])
        self.fill_input(self.locators.LASTNAME_INPUT, user['surname'])
        self.fill_input(self.locators.USERNAME_INPUT, user['username'])
        self.fill_input(self.locators.EMAIL_INPUT, user['email'])
        self.fill_input(self.locators.PASSWORD_INPUT, user['psw'])
        try:
            self.fill_input(self.locators.PASSWORD_CONFIRM_INPUT, user['psw'])
        except Exception:
            pass

    @allure.step("Отправить форму регистрации")
    def submit_registration(self):
        self.click_on_element(self.locators.CREATE_ACC_BTN)

    @allure.step("Зарегистрировать аккаунт")
    def register_user(self, user: dict):
        self.fill_registration_form(user)
        self.submit_registration()
