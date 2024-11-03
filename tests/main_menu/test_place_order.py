from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestPlaceOrder:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)

    def test_place_order(self):
        # Переходим на страницу входа
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Ожидаем, пока ингредиент станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"))
        )

        # Нажимаем на ингредиент и перетаскиваем его в правую часть экрана
        self.main_page.drag_and_drop_ingredient()

        # Нажимаем кнопку "Оформить заказ"
        self.main_page.click_place_order_button()

        # Ожидаем появления локатора идентификатора заказа
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'идентификатор заказа')]"))
        )

        # Проверяем, что отображается локатор идентификатора заказа
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'идентификатор заказа')]").is_displayed(), "Идентификатор заказа не найден."
