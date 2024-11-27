from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from reset_password_page_locators import ResetPasswordPageLocators  # Импортируем локаторы
from ..urls import URLS  # Импортируем URL-константы

class ResetPasswordPage(BasePage):  # Наследуем от BasePage
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        """Переход на страницу восстановления пароля"""
        self.driver.get(URLS["forgot_password_page"])

    def enter_email(self, email):
        """Ввод email в поле"""
        email_input = self.find_element(ResetPasswordPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def click_recover_button(self):
        """Клик по кнопке 'Восстановить пароль'"""
        self.click_element(ResetPasswordPageLocators.RECOVER_BUTTON)

    def is_password_reset_heading_visible(self):
        """Проверка видимости заголовка 'Восстановление пароля'"""
        heading = self.find_element(ResetPasswordPageLocators.HEADING)
        return heading.is_displayed()

    def click_eye_button(self):
        """Клик по кнопке 'показать/скрыть пароль'"""
        self.click_element(ResetPasswordPageLocators.EYE_BUTTON)

    def is_password_input_active(self):
        """Проверка, что поле для пароля активно"""
        password_input = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_input.is_displayed() and "input_status_active" in password_input.find_element(By.XPATH, "..").get_attribute("class")

    def get_password_input_type(self):
        """Получение текущего типа поля ввода пароля ('password' или 'text')"""
        password_input = self.find_element(ResetPasswordPageLocators.NEW_PASSWORD_INPUT)
        return password_input.get_attribute("type")

    def is_password_reset_successful(self):
        """Проверяем, что редирект на страницу восстановления пароля успешен"""
        return self.driver.current_url == URLS["forgot_password_page"]

    def wait_for_url_to_be(self, url, timeout=10):
        """Ожидаем, пока текущий URL станет равен указанному"""
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_password_input_type(self, expected_type, timeout=10):
        """Ожидаем изменения типа поля ввода пароля"""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(
                ResetPasswordPageLocators.NEW_PASSWORD_INPUT, 'type', expected_type
            )
        )
