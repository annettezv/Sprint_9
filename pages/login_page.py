import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step("Дождаться отображения формы авторизации")
    def wait_for_login_form(self):
        self.wait_visibility_of_element(self.locators.EMAIL_INPUT)
        self.wait_visibility_of_element(self.locators.PASSWORD_INPUT)
        self.wait_visibility_of_element(self.locators.LOGIN_BTN)
        return True

    @allure.step("Авторизовать пользователя")
    def login(self, username: str, password: str):
        self.wait_for_login_form()
        self.fill_input(self.locators.EMAIL_INPUT, username)
        self.fill_input(self.locators.PASSWORD_INPUT, password)
        self.click_on_element(self.locators.LOGIN_BTN)
        