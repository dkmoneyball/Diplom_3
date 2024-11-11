import pytest
from pages.main_page import MainPage

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
        self.main_page.verify_url("https://stellarburgers.nomoreparties.site/")
