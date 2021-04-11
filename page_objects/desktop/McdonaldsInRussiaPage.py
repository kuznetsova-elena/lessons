from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class McdonaldsInRussiaPage(BasePage):
    URL = "/page/mcdonalds_in_russia/"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.contacts__heading-title.mcd__russia-title.-center-xs")
