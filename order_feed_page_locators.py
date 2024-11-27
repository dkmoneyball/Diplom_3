from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    FIRST_ORDER = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//li[1]//a[1]")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'order-feed')]//li")
