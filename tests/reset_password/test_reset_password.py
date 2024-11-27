import pytest
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
from ..urls import URLS  # URL вынесен в константы

class TestPasswordRecovery:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.reset_password_page = ResetPasswordPage(driver)
        self.login_page = LoginPage(driver)  # Инициализация LoginPage

    def test_recover_password(self):
        # Переход на страницу входа
        self.driver.get(URLS["login_page"])

        # Нажимаем на кнопку "Восстановить пароль"
        self.login_page.click_reset_password_button()

        # Ожидаем редирект на страницу восстановления пароля
        self.reset_password_page.wait_for_url_to_be(URLS["forgot_password_page"])

        # Проверяем, что редирект действительно произошел
        assert self.reset_password_page.is_password_reset_successful(), "Редирект на страницу восстановления пароля не произошел."
