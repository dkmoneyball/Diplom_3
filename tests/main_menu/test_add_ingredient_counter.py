from pages.main_page import MainPage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddIngredientCounter:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_add_ingredient_counter(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # Ожидаем, пока страница полностью загрузится
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"))
        )

        # Нажимаем на ингредиент и перетаскиваем его в правую часть экрана
        self.main_page.drag_and_drop_ingredient()

        # Ожидаем, пока появится текст с новым счетчиком ингредиентов
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'1976')]"))
        )

        # Проверяем, что мы видим нужный счетчик
        counter_text = self.driver.find_element(By.XPATH, "//p[contains(text(),'1976')]").text
        assert counter_text == '1976', "Счетчик ингредиента не увеличился."
