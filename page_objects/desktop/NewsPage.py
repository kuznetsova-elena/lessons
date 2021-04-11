from page_objects.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WorkAtMcdonaldsPage(BasePage):
    URL = "/rabota-v-mcdonalds"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-vacancies__title")
