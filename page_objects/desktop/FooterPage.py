from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class FooterPage(BasePage):
    ABOUT_US_TITLE = (By.XPATH, "//div/span[contains(., 'О нас')]")
    CONTACTS_TITLE = (By.XPATH, "//div/span[contains(., 'Контакты')]")
    SUBSCRIBE_TITLE = (By.XPATH, "//div/span[contains(., 'Подписывайтесь на рассылку')]")
    WORK_IN_MCDONALDS = (By.LINK_TEXT, "Работа в Макдоналдс")

    def is_title_present(self, title):
        element = self.browser.find_element(title)
        return element
