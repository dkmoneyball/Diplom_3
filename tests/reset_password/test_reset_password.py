from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.reset_password_page import ResetPasswordPage

class TestPasswordRecovery:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.reset_password_page = ResetPasswordPage(driver)

    def test_recover_password(self):
        # Переход на страницу восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

        # Нажимаем на кнопку "Восстановить пароль"
        self.reset_password_page.click_reset_password_button()

        # Ожидаем редирект на страницу восстановления пароля и проверяем URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password")
        )

        # Проверяем, что редирект действительно произошел
        assert self.reset_password_page.is_password_reset_successful(), "Редирект на страницу восстановления пароля не произошел."
