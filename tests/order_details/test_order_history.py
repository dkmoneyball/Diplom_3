import pytest
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from ..urls import URLS  # Импортируем URL из urls.py

class TestOrderHistory:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.order_feed_page = OrderFeedPage(driver)
        self.login_page = LoginPage(driver)

    def test_orders_displayed_in_feed(self):
        # Переходим на страницу входа
        self.driver.get(URLS["login_page"])

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переходим на Ленту заказов
        self.driver.get(f"{URLS['home_page']}feed")  # Используем BASE_URL

        # Ожидаем, пока заказ с номером '#0151302' станет видимым
        self.order_feed_page.wait_for_order_to_be_visible('#0154404')

        # Проверяем, что заказ отображается
        assert self.order_feed_page.is_order_displayed('#0154404'), "Заказ не найден на странице Ленты заказов."
