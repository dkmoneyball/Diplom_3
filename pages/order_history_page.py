from pages.base_page import BasePage
from order_history_page_locators import OrderHistoryPageLocators  # Импортируем локаторы

class OrderHistoryPage(BasePage):  # Наследуем от BasePage
    def __init__(self, driver):
        super().__init__(driver)

    def get_orders(self):
        orders = []
        order_elements = self.driver.find_elements(*OrderHistoryPageLocators.ORDER_ELEMENTS)
        for order in order_elements:
            order_number = order.find_element(*OrderHistoryPageLocators.ORDER_NUMBER).text
            orders.append(order_number)
        return orders
