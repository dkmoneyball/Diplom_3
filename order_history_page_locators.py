from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    ORDER_ELEMENTS = (By.XPATH, "//div[contains(@class, 'order-element')]")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'order-number')]")
