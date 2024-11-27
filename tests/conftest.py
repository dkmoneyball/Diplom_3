import pytest
from selenium import webdriver
from urls import URLS  # Импортируем константы URL-адресов

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()  # или используйте другой драйвер
    driver.get(URLS["login_page"])  # Используем URL из констант
    yield driver
    driver.quit()
