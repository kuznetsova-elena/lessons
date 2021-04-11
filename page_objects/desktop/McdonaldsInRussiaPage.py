from page_objects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class McdonaldsInRussiaPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.contacts__heading-title mcd__russia-title -center-xs")


