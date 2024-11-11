from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.base_page import BasePage
from login_page_locators import LoginPageLocators  # Импортируем локаторы

class LoginPage(BasePage):  # Наследуем от BasePage
    def __init__(self, driver):
        super().__init__(driver)  # Инициализируем базовый класс

    def open(self, url="https://stellarburgers.nomoreparties.site/login"):
        """Переход на страницу входа"""
        self.driver.get(url)

    def enter_email(self, email):
        email_input = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def click_reset_password_button(self):
        reset_button = self.find_element(LoginPageLocators.RESET_PASSWORD_BUTTON)
        reset_button.click()

    def open_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

