# test_place_order.py
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from main_page_locators import MainPageLocators


class TestPlaceOrder:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)

    def test_place_order(self):
        # Переходим на страницу входа
        self.login_page.open_page()  # Переход через Page Object

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Ожидаем, пока ингредиент станет видимым
        self.main_page.wait_for_element_to_be_visible(MainPageLocators.INGREDIENT_BUTTON)

        # Локаторы для ингредиента и области перетаскивания
        ingredient_locator = MainPageLocators.INGREDIENT_BUTTON
        drop_area_locator = MainPageLocators.DROP_AREA

        # Нажимаем на ингредиент и перетаскиваем его в правую часть экрана
        self.main_page.drag_and_drop(ingredient_locator, drop_area_locator)

        # Нажимаем кнопку "Оформить заказ"
        self.main_page.click_place_order_button()

        # Ожидаем появления идентификатора заказа
        self.main_page.wait_for_order_identifier()

        # Проверяем, что отображается локатор идентификатора заказа
        assert self.driver.find_element(By.XPATH,
                                        "//p[contains(text(),'идентификатор заказа')]").is_displayed(), "Идентификатор заказа не найден."
