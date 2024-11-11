from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from main_page_locators import MainPageLocators  # Импортируем локаторы

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url="https://stellarburgers.nomoreparties.site/"):
        """Метод для перехода на страницу."""
        self.driver.get(url)

    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed_button(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_on_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_BUTTON)

    def close_popup(self):
        self.click_element(MainPageLocators.POPUP_CLOSE_BUTTON)

    def drag_and_drop_ingredient(self, ingredient_locator, drop_area_locator):
        """Перетаскиваем ингредиент в нужную область."""
        self.drag_and_drop(ingredient_locator, drop_area_locator)

    def click_place_order_button(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_ingredient_counter(self):
        """Получаем текст с счетчиком ингредиентов."""
        return self.find_element(MainPageLocators.INGREDIENT_COUNTER).text

    def wait_for_ingredient_counter(self, counter_text, time=10):
        """Ожидаем появления счетчика ингредиентов с указанным текстом."""
        counter_locator = (By.XPATH, f"//p[contains(text(),'{counter_text}')]")
        self.wait_for_element_to_be_visible(counter_locator, time)

    def wait_for_ingredient_details_header(self, time=10):
        """Ожидаем появления заголовка 'Детали ингредиента'"""
        self.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_DETAILS_HEADER, time)

    def verify_url(self, expected_url):
        """Проверяем, что текущий URL соответствует ожидаемому"""
        assert self.driver.current_url == expected_url, f"Ожидаемый URL {expected_url}, но текущий: {self.driver.current_url}"

    def wait_for_order_identifier(self, time=10):
        """Ожидаем появления идентификатора заказа"""
        self.wait_for_element_to_be_visible(MainPageLocators.ORDER_IDENTIFIER, time)
