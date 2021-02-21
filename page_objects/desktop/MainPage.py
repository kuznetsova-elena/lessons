from page_objects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    BANNER_SLIDER = (By.CSS_SELECTOR, "div.base-slider__wrap.swiper-wrapper > div:nth-child(1)")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, "button.mini-cart__button")
    PRODUCT_SNIPPET = (By.CSS_SELECTOR, "ul.menu-catalog > li:nth-child(1)")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div.base-modal__body>div>div>div>div>div>div:nth-child(2)>button>span")

    def click_product(self, product_locator):
        self._click(product_locator)

    def add_to_cart(self):
        self._click(self.ADD_TO_CART_BUTTON)

    def open_cart(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.OPEN_CART_BUTTON)).click()

    def is_element_present(self, locator):
        return self.browser.find_elements(*locator)