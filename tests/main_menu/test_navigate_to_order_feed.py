import pytest
from pages.main_page import MainPage
from ..urls import URLS  # Импортируем константы URL

class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_navigate_to_order_feed(self):
        # Используем URL для главной страницы из констант
        self.driver.get(URLS["home_page"])

        # Нажимаем на кнопку "Лента заказов"
        self.main_page.click_order_feed_button()

        # Проверяем, что URL соответствует ожидаемому
        self.main_page.verify_url(URLS["order_feed_page"])
