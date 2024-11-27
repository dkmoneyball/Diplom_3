import pytest
from pages.main_page import MainPage
from ..urls import URLS  # Импортируем константы URL

class TestNavigateToConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_navigate_to_constructor(self):
        # Используем URL для главной страницы из констант
        self.driver.get(URLS["home_page"])

        # Переход по клику на «Конструктор»
        self.main_page.click_constructor_button()

        # Проверяем, что URL соответствует ожидаемому
        self.main_page.verify_url(URLS["home_page"])
