import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Подождать кликабельности элемента")
    def wait_element_to_be_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )
    
    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).click()
    
    @allure.step("Кликнуть на элемент через JavaScript")
    def click_on_element_js(self, locator):
        element = self.wait_visibility_of_element(locator)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Заполнить поле")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Сравнить текущий URL страницы с ожидаемым")
    def check_current_page_url(self, expected_url):
        assert self.driver.current_url == expected_url
    
    @allure.step("Подождать видимости элемента")
    def wait_visibility_of_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
    
    @allure.step("Подождать исчезновения элемента")
    def wait_invisibility_of_element(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
