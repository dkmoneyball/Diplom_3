from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResetPasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        # Ожидаем, пока поле ввода email станет видимым
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]"))
        )
        email_input.clear()  # Очищаем поле, если там что-то есть
        email_input.send_keys(email)  # Вводим email

    def click_recover_button(self):
        # Ожидаем, пока кнопка "Восстановить" станет кликабельной
        recover_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Восстановить')]"))
        )
        recover_button.click()  # Нажимаем на кнопку "Восстановить"

    def is_password_reset_heading_visible(self):
        # Проверяем, что заголовок "Восстановление пароля" виден
        heading = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Восстановление пароля')]"))
        )
        return heading.is_displayed()

    def click_eye_button(self):
        # Ожидаем, пока кнопка "глазик" станет кликабельной
        eye_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]"))
        )
        eye_button.click()  # Нажимаем на кнопку "глазик"

    def is_password_input_active(self):
        # Ожидаем, пока поле ввода пароля станет видимым
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[@class='input pr-6 pl-6 input_type_password input_size_default input_status_active']/input"))
        )

        # Проверяем, что поле ввода отображается
        is_displayed = password_input.is_displayed()

        # Проверяем, что поле ввода имеет активный статус
        is_active = "input_status_active" in password_input.find_element(By.XPATH, "..").get_attribute("class")

        return is_displayed and is_active

    def get_password_input_type(self):
        # Ожидаем, пока поле ввода пароля станет видимым
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//input[@name='Введите новый пароль']"))
        )
        return password_input.get_attribute("type")  # Возвращаем тип поля ввода
