import pytest
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.personal_account_page = PersonalAccountPage(driver)

    def test_logout(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Вводим email и пароль
        self.login_page.enter_email("danilll@mail.ru")
        self.login_page.enter_password("123456789")

        # Нажимаем на кнопку "Войти"
        self.login_page.click_login_button()

        # Переход в Личный кабинет
        self.personal_account_page.click_personal_account_button()

        # Нажимаем на кнопку "Выход"
        self.personal_account_page.click_logout_button()

        # Ожидаем, пока произойдет редирект на страницу входа
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/login")
        )

        # Проверяем, что мы перешли на правильный URL
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login", "Выход из аккаунта не удался."
