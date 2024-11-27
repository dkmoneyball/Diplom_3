import pytest
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from ..urls import URLS  # Импортируем константы URL

class TestLogout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.personal_account_page = PersonalAccountPage(driver)

    def test_logout(self):
        # Переходим на страницу входа с использованием URL из констант
        self.driver.get(URLS["login_page"])

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переход в Личный кабинет
        self.personal_account_page.click_personal_account_button()

        # Нажимаем на кнопку "Выход"
        self.personal_account_page.click_logout_button()

        # Ожидаем редирект на страницу входа
        self.personal_account_page.wait_for_logout_redirect()

        # Проверяем, что URL соответствует ожидаемому
        assert self.driver.current_url == URLS["login_page"], "Выход из аккаунта не удался."
