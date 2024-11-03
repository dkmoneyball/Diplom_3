from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='Пароль']"))
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        # Ожидаем, пока кнопка "Войти" станет кликабельной
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти')]"))
        )
        # Используем JavaScript для клика, если возникает ошибка
        self.driver.execute_script("arguments[0].click();", login_button)

    def click_reset_password_button(self):
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Восстановить пароль')]"))
        )
        reset_button.click()