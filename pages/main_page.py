from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li[1]//a[1]")  # Кнопка "Конструктор"
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # Кнопка "Лента Заказов"
    INGREDIENT_BUTTON = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")  # Локатор ингредиента (замените на правильный)
    POPUP_CLOSE_BUTTON = (By.XPATH, "//body/div[@id='root']/div[1]/section[1]/div[1]/button[1]/*[1]")  # Крестик закрывающего всплывающего окна
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"
    INGREDIENT_COUNTER = (By.XPATH, "//span[@class='ingredient-counter']")  # Локатор счетчика ингредиента (замените на правильный)

    def click_constructor_button(self):
        constructor_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

    def click_order_feed_button(self):
        order_feed_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ORDER_FEED_BUTTON)
        )
        order_feed_button.click()

    def click_on_ingredient(self):
        ingredient_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.INGREDIENT_BUTTON)
        )
        ingredient_button.click()

    def close_popup(self):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.POPUP_CLOSE_BUTTON)
        )
        close_button.click()

    def drag_and_drop_ingredient(self):
        # Здесь необходимо реализовать логику перетаскивания ингредиента
        # Пример: используйте ActionChains для перетаскивания ингредиента
        from selenium.webdriver import ActionChains

        ingredient_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.INGREDIENT_BUTTON)
        )
        drop_area = self.driver.find_element(By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Локатор области, куда нужно перетащить

        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient_element).move_to_element(drop_area).release().perform()

    def click_place_order_button(self):
        place_order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        )
        place_order_button.click()

    def get_ingredient_counter(self):
        counter_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.INGREDIENT_COUNTER)
        )
        return int(counter_element.text)  # Предполагается, что текст - это число
