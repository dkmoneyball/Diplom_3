from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    HEADING = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    EYE_BUTTON = (By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]")
    PASSWORD_INPUT = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default input_status_active']/input")
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")