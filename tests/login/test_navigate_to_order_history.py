import pytest
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from ..urls import URLS  # Импортируем константы URL

class TestNavigateToOrderHistory:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.personal_account_page = PersonalAccountPage(driver)

    def test_navigate_to_order_history(self):
        # Переход на страницу входа с использованием URL из констант
        self.driver.get(URLS["login_page"])

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переход в Личный кабинет
        self.personal_account_page.click_personal_account_button()

        # Переход в Историю заказов
        self.personal_account_page.click_order_history()

        # Ожидаем редирект на страницу Истории заказов
        self.personal_account_page.wait_for_order_history_page()

        # Проверяем, что URL соответствует ожидаемому
        assert self.driver.current_url == URLS["order_history_page"], "Переход в Историю заказов не удался."
