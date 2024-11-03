from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestOrderHistory:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.order_feed_page = OrderFeedPage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)

    def test_orders_displayed_in_feed(self):
        # Переходим на страницу входа
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переходим на Ленту заказов
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

        # Ожидаем, пока элемент с номером заказа станет видимым
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='#0149762']"))
        )

        # Проверяем, что локатор заказа отображается на странице
        assert self.driver.find_element(By.XPATH, "//p[normalize-space()='#0149762']").is_displayed(), "Заказ не найден на странице Ленты заказов."
