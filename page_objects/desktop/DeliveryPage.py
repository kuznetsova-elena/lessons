from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class DeliveryPage(BasePage):
    URL = "/menu/delivery"

    PAGE_TITLE = (By.CSS_SELECTOR, "a.delivery__link.nuxt-link-exact-active.nuxt-link-active > span")
