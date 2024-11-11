import pytest
from selenium.webdriver.common.by import By  # Добавляем импорт By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reset_password_page import ResetPasswordPage

class TestTogglePasswordVisibility:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.reset_password_page = ResetPasswordPage(driver)

    def test_toggle_password_visibility(self):
        # Переход на страницу восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # Вводим email
        self.reset_password_page.enter_email("1411test@example.com")

        # Нажимаем на кнопку "Восстановить"
        self.reset_password_page.click_recover_button()

        # Проверяем, что тип поля ввода пароля изначально 'password'
        assert self.reset_password_page.get_password_input_type() == "password"

        # Нажимаем на кнопку "показать/скрыть пароль"
        self.reset_password_page.click_eye_button()

        # Ожидаем, что тип поля ввода изменится на 'text'
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, "//input[@name='Введите новый пароль']"), 'type', 'text'
            )
        )

        # Проверяем, что тип поля ввода изменился на 'text'
        assert self.reset_password_page.get_password_input_type() == "text"
