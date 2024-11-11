from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from personal_account_page_locators import PersonalAccountPageLocators

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_account_button(self):
        self.click_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_order_history(self):
        self.click_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    def wait_for_logout_redirect(self, time=10):
        """Ожидаем редиректа на страницу входа после выхода"""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )

    def wait_for_order_history_page(self, time=10):
        """Ожидаем редиректа на страницу истории заказов"""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account/order-history")
        )

    def wait_for_personal_account_page(self, time=10):
        """Ожидаем редиректа на страницу Личного кабинета"""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/account")
        )

