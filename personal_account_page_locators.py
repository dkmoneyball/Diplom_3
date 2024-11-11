from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
