from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestOrderFeed:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.order_feed_page = OrderFeedPage(driver)
        self.login_page = LoginPage(driver)

    def test_place_order_and_check_details(self):
        # Переходим на страницу входа
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переходим на Ленту заказов
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

        # Нажимаем на первый заказ
        self.order_feed_page.click_on_first_order()

        # Проверяем, что текст "Состав" отображается
        assert self.driver.find_element(By.XPATH, "//p[contains(text(),'Cостав')]").is_displayed(), "Текст 'Состав' не найден."
