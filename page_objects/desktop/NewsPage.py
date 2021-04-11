from page_objects.BasePage import BasePage

from selenium.webdriver.common.by import By


class NewsPage(BasePage):
    URL = "/articles/news"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-heading__title")
