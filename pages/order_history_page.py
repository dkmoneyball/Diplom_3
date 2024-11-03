
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderHistoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_orders(self):
        # Получаем список заказов из истории
        orders = []
        order_elements = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'order-element')]")  # Предположительный локатор
        for order in order_elements:
            order_number = order.find_element(By.XPATH, ".//p[contains(@class, 'order-number')]").text
            orders.append(order_number)
        return orders
