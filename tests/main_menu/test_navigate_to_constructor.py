# test_navigate_to_constructor.py
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import pytest

class TestNavigateToConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_navigate_to_constructor(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # Переход по клику на «Конструктор»
        self.main_page.click_constructor_button()

        # Проверяем, что URL соответствует ожидаемому
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/", "Переход на Конструктор не удался."
