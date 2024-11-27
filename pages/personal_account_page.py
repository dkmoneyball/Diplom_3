from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from personal_account_page_locators import PersonalAccountPageLocators
from ..urls import URLS  # Импортируем URL-константы

class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_account_button(self):
        """Клик по кнопке 'Личный кабинет'."""
        self.click_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def click_order_history(self):
        """Клик по кнопке 'История заказов'."""
        self.click_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        """Клик по кнопке 'Выход'."""
        self.click_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    def wait_for_logout_redirect(self, time=10):
        """Ожидаем редиректа на страницу входа после выхода."""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be(URLS["login_page"])  # Используем URL из констант
        )

    def wait_for_order_history_page(self, time=10):
        """Ожидаем редиректа на страницу Истории заказов."""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be(URLS["order_history_page"])  # Используем URL из констант
        )

    def wait_for_personal_account_page(self, time=10):
        """Ожидаем редиректа на страницу Личного кабинета."""
        WebDriverWait(self.driver, time).until(
            EC.url_to_be(URLS["personal_account_page"])  # Используем URL из констант
        )
