from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class FeedbackPage(BasePage):
    URL = "/page/contacts/feedback"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.contacts__heading-title")
