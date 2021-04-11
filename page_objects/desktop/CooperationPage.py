from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class CooperationPage(BasePage):
    URL = "/page/contacts/cooperation"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.contacts__heading-title.-center-xs")
