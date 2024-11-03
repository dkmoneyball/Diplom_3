from pages.main_page import MainPage
import pytest


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
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/feed", "Переход в Ленту заказов не удался."
