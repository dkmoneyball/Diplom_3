from selenium.webdriver.common.by import By  # Добавляем импорт
from pages.base_page import BasePage
from order_feed_page_locators import OrderFeedPageLocators  # Импортируем локаторы

class OrderFeedPage(BasePage):  # Наследуем от BasePage
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_first_order(self):
        self.click_element(OrderFeedPageLocators.FIRST_ORDER)

    def get_orders(self):
        order_elements = self.driver.find_elements(*OrderFeedPageLocators.ORDER_LIST)
        return order_elements

    def check_composition_text(self):
        """Проверяем, что текст 'Состав' присутствует на странице заказа"""
        composition_locator = "//p[contains(text(),'Cостав')]"
        self.wait_for_element_to_be_visible((By.XPATH, composition_locator))
        return self.find_element((By.XPATH, composition_locator)).is_displayed()

    def wait_for_order_to_be_visible(self, order_number, time=10):
        """Ожидаем, пока заказ с указанным номером станет видимым"""
        order_locator = (By.XPATH, f"//p[normalize-space()='{order_number}']")
        self.wait_for_element_to_be_visible(order_locator, time)

    def is_order_displayed(self, order_number):
        """Проверяем, что заказ с указанным номером отображается на странице"""
        order_locator = (By.XPATH, f"//p[normalize-space()='{order_number}']")
        return self.is_element_present(order_locator)