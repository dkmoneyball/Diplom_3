import pytest
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from ..urls import URLS  # Импортируем URL из urls.py

class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.order_feed_page = OrderFeedPage(driver)
        self.login_page = LoginPage(driver)

    def test_place_order_and_check_details(self):
        # Переходим на страницу входа
        self.driver.get(URLS["login_page"])

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переходим на Ленту заказов
        self.driver.get(f"{URLS['home_page']}feed")

        # Нажимаем на первый заказ
        self.order_feed_page.click_on_first_order()

        # Проверяем, что текст "Состав" отображается
        assert self.order_feed_page.check_composition_text(), "Текст 'Состав' не найден."
