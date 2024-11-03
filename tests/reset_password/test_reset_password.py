import pytest
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.reset_password_page = ResetPasswordPage(driver)

    def test_recover_password(self):
        # Переход на страницу восстановления пароля
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # Вводим email
        self.reset_password_page.enter_email("test@example.com")  # Замените на любой тестовый email

        # Нажимаем на кнопку "Восстановить"
        self.reset_password_page.click_recover_button()

        # Здесь можно добавить проверки, что действие прошло успешно
        # Например, проверка, что отображается сообщение об успешной отправке письма
