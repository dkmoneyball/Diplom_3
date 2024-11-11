import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()  # или используйте другой драйвер
    driver.get("https://stellarburgers.nomoreparties.site/login")  # Загружаем страницу входа
    yield driver
    driver.quit()
