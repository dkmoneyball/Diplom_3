import pytest
from pages.reset_password_page import ResetPasswordPage
from ..urls import URLS

class TestTogglePasswordVisibility:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.reset_password_page = ResetPasswordPage(driver)

    def test_toggle_password_visibility(self):
        # Переход на страницу восстановления пароля
        self.driver.get(f"{URLS['home_page']}forgot-password")

        # Вводим email
        self.reset_password_page.enter_email("1411test@example.com")

        # Нажимаем на кнопку "Восстановить"
        self.reset_password_page.click_recover_button()

        # Проверяем, что тип поля ввода пароля изначально 'password'
        assert self.reset_password_page.get_password_input_type() == "password"

        # Нажимаем на кнопку "показать/скрыть пароль"
        self.reset_password_page.click_eye_button()

        # Ожидаем, что тип поля ввода изменится на 'text'
        self.reset_password_page.wait_for_password_input_type("text")

        # Проверяем, что тип поля ввода изменился на 'text'
        assert self.reset_password_page.get_password_input_type() == "text"
