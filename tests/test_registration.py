
import allure
from configs.urls import Urls
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from locators.base_page_locators import BasePageLocators


class TestRegistration:

    @allure.title("Регистрация нового аккаунта ведет на страницу авторизации")
    def test_registration_new_acc(self, driver, user):
        base_page = BasePage(driver)
        base_page.click_on_element(BasePageLocators.CREATE_ACC_BTN)
        reg_page = RegistrationPage(driver)
        reg_page.register_user(user)
        login_page = LoginPage(driver)
        assert login_page.wait_for_login_form() is True
        current_url = base_page.get_current_url()
        assert "/signin" in current_url or current_url.startswith(Urls.LOGIN_PAGE)
