from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def find_element(self, locator, time=10):
        """Найти элемент на странице с ожиданием"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, time=10):
        """Кликнуть по элементу"""
        element = self.find_element(locator, time)
        element.click()

    def is_element_present(self, locator, time=10):
        """Проверка наличия элемента на странице"""
        try:
            self.find_element(locator, time)
            return True
        except:
            return False

    def scroll_to_bottom(self):
        """Прокрутить страницу до конца"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_text_present(self, locator, expected_text, time=10):
        """Проверить, что на странице присутствует ожидаемый текст"""
        element = self.find_element(locator, time)
        return expected_text in element.text

    def fill_input(self, locator, text, time=10):
        """Заполнить поле ввода"""
        element = self.find_element(locator, time)
        element.clear()  # Очистить поле перед вводом
        element.send_keys(text)

    def drag_and_drop(self, source_locator, target_locator, time=10):
        """Перетащить элемент из одного места в другое"""
        source_element = self.find_element(source_locator, time)
        target_element = self.find_element(target_locator, time)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source_element).move_to_element(target_element).release().perform()

    def wait_for_element_to_be_visible(self, locator, time=10):
        """Ожидаем, пока элемент станет видимым"""
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )
