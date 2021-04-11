import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    INSTAGRAM = "https://www.instagram.com/mcdonalds_rus/?hl=ru"
    FACEBOOK = "https://www.facebook.com/mcdonaldsrussia/"
    VK = "https://vk.com/mcdonaldsrussia"
    YOUTUBE = "https://www.youtube.com/channel/UCvRH4-D8PEk2zdyprlWKs-g"
    VIBER = "viber://chat/?number=%2B79265221143"
    WHATSAPP = "https://api.whatsapp.com/send/?phone=%2B79265221143&text&app_absent=0"
    APP_STORE_URL = "https://apps.apple.com/ru/app/%D0%BC%D0%B0%D0%BA%D0%B4%D0%BE%D0%BD%D0%B0%D0%BB%D0%B4%D1%81" \
                    "/id896111038"
    GOOGLE_PLAY_URL = "https://play.google.com/store/apps/details?id=com.apegroup.mcdonaldsrussia&hl=ru"
    APP_GALLERY_URL = "https://appgallery.huawei.com/#/app/C102465481"

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Выполняю клик по элементу {locator}")
    def _click(self, locator: tuple):
        self.verify_element_on_page(locator).click()

    @allure.step("Проверяю наличие элемента на странице")
    def verify_element_on_page(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot("exception.png")
            raise AssertionError("Элемент {} не найден на странице".format(locator))

    @allure.step("Клик по ссылке")
    def click_link(self, locator: tuple):
        self.browser.find_element(*locator).click()

    @allure.step("Проверяю наличие текста на странице")
    def is_text_presented_on_page(self, locator: tuple):
        element = self.browser.find_element(*locator)
        return element

    @allure.step("Клик по кнопке {locator}")
    def go_to_third_party_site(self, locator: tuple):

        old_tabs = self.browser.window_handles
        self.verify_element_on_page(locator)
        new_tabs = self.browser.window_handles
        for tab in new_tabs:
            if tab in old_tabs:
                pass
            else:
                new_tab = tab
                self.browser.switch_to.window(new_tab)

    def find_element(self, locator: tuple):
        return WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))

    def cannot_find_element(self, locator: tuple):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return "NoSuchElementException"
