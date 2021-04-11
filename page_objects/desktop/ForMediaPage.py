from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class ForMediaPage(BasePage):
    URL = "/page/contacts/media"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.contacts__heading-title.-center-xs")
