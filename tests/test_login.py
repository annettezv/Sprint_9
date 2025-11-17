from selenium import webdriver
import allure
from configs.urls import Urls
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from locators.base_page_locators import BasePageLocators


class TestAuthorization:

    @allure.title("Авторизация пользователя: переход на главную и отображение кнопки 'Выход'")
    def test_register_then_login(self, driver, user):
        base_page = BasePage(driver)

        base_page.click_on_element(BasePageLocators.CREATE_ACC_BTN)
        reg_page = RegistrationPage(driver)
        reg_page.register_user(user)

        login_page = LoginPage(driver)
        assert login_page.wait_for_login_form() is True
        login_page.login(username=user["username"], password=user["psw"])

        assert base_page.get_current_url().startswith(Urls.BASE_PAGE_URL)
        base_page.wait_visibility_of_element(BasePageLocators.LOGOUT_BTN)
