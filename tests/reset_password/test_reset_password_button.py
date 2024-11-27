import pytest
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from ..urls import URLS


class TestResetPassword:
    @pytest.fixture(autouse=True)
    def setup(self, driver):  # driver - это фикстура, определенная в conftest.py
        self.driver = driver  # Присваиваем driver в self.driver
        self.login_page = LoginPage(driver)
        self.reset_password_page = ResetPasswordPage(driver)

    def test_navigate_to_reset_password(self):
        # Переход на страницу входа
        self.driver.get(URLS["login_page"])

        # Нажимаем на кнопку "Восстановить пароль"
        self.login_page.click_reset_password_button()

        # Проверяем, что заголовок "Восстановление пароля" отображается
        assert self.reset_password_page.is_password_reset_heading_visible()
