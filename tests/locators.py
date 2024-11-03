from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    CODE_INPUT = (By.XPATH, "//input[@placeholder='Введите код из письма']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    HEADING = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    EYE_BUTTON = (By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/div[1]/svg[1]/path[1]")
    EMAIL_INPUT = (By.XPATH,
                   "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")  # Локатор для поля ввода email

