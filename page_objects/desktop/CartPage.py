from selenium.webdriver.common.by import By


class CartPage:
    URL = "/cart"
    TITLE = (By.CLASS_NAME, 'cart-drawer__header')
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[text="Очистить"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[class="el-drawer__close-btn"]')
