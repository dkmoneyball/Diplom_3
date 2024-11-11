# test_add_ingredient_details.py
from main_page_locators import MainPageLocators
import pytest
from pages.main_page import MainPage

class TestAddIngredientDetails:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_show_ingredient_details(self):
        # Переходим на главную страницу
        self.main_page.open_page()

        # Ожидаем, пока ингредиент станет видимым
        self.main_page.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_BUTTON)

        # Нажимаем на ингредиент
        self.main_page.click_on_ingredient()

        # Ожидаем, пока появится заголовок "Детали ингредиента"
        self.main_page.wait_for_ingredient_details_header()

        # Проверяем, что заголовок "Детали ингредиента" присутствует
        assert self.driver.find_element(*MainPageLocators.INGREDIENT_DETAILS_HEADER).is_displayed(), "Заголовок 'Детали ингредиента' не отображается."
