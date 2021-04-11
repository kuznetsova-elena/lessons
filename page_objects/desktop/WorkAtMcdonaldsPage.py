from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class WorkAtMcdonaldsPage(BasePage):
    URL = "/rabota-v-mcdonalds"
    LINK = "Работа в Макдоналдс"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-vacancies__title")
