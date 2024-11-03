from pages.main_page import MainPage
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddIngredientDetails:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def test_show_ingredient_details(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/")

        # Нажимаем на ингредиент
        self.main_page.click_on_ingredient()

        # Проверяем, что заголовок "Детали ингредиента" присутствует
        header_locator = "//h2[contains(text(),'Детали ингредиента')]"
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, header_locator))
        )

        # Если вы хотите сделать дополнительную проверку, вы можете это сделать
        assert self.driver.find_element(By.XPATH, header_locator).is_displayed(), "Заголовок 'Детали ингредиента' не отображается."
