from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class CharityPage(BasePage):
    URL = "/page/charity/"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.charity-header__text")
