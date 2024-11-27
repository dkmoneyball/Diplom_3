from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
