# test_add_ingredient_counter.py
from main_page_locators import MainPageLocators
import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By

class TestAddIngredientCounter:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_add_ingredient_counter(self):
        self.main_page.open_page()

        # Ожидаем, пока ингредиент станет видимым
        self.main_page.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_BUTTON)

        # Локаторы ингредиента и области для перетаскивания
        ingredient_locator = MainPageLocators.INGREDIENT_BUTTON
        drop_area_locator = MainPageLocators.DROP_AREA

        # Перетаскиваем ингредиент
        self.main_page.drag_and_drop_ingredient(ingredient_locator, drop_area_locator)

        # Ожидаем, пока появится счетчик
        self.main_page.wait_for_ingredient_counter('1976')

        # Проверяем, что счетчик ингредиентов увеличился
        counter_text = self.main_page.get_ingredient_counter()
        assert counter_text == '1976', "Счетчик ингредиента не увеличился."
