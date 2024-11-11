from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для кнопок и элементов
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li[1]//a[1]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    INGREDIENT_BUTTON = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//body/div[@id='root']/div[1]/section[1]/div[1]/button[1]/*[1]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(text(),'1976')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")
    ORDER_IDENTIFIER = (By.XPATH, "//p[contains(text(),'идентификатор заказа')]")
    DROP_AREA = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
