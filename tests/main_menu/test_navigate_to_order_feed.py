import pytest
from pages.main_page import MainPage

class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_navigate_to_order_feed(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на кнопку "Лента заказов"
        self.main_page.click_order_feed_button()

        # Проверяем, что URL соответствует ожидаемому
        self.main_page.verify_url("https://stellarburgers.nomoreparties.site/feed")
