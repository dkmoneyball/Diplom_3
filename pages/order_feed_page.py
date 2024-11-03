from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderFeedPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_on_first_order(self):
        # Локатор для первого заказа
        order_locator = "//main[@class='App_componentContainer__2JC2W']//li[1]//a[1]"
        order_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, order_locator))
        )
        order_element.click()

    def get_orders(self):
        # Находим все элементы заказов на странице
        return self.driver.find_elements(By.XPATH, "//ul[contains(@class, 'order-feed')]//li")