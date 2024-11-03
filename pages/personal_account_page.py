from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_personal_account_button(self):
        personal_account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))
        )
        personal_account_button.click()

    def click_order_history(self):
        order_history_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'История заказов')]"))
        )
        order_history_button.click()

    def click_logout_button(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Выход')]"))
        )
        logout_button.click()
