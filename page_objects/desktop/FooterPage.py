import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.BasePage import BasePage


class FooterPage(BasePage):
    ABOUT_US_TITLE = (By.XPATH, "//span[contains(., 'О нас')]")
    CONTACTS_TITLE = (By.XPATH, "//div/span[contains(., 'Контакты')]")
    SUBSCRIBE_TITLE = (By.XPATH, "//div/span[contains(., 'Подписывайтесь на рассылку')]")

    WORK_IN_MCDONALDS = (By.LINK_TEXT, "Работа в Макдоналдс")
    MCDONALDS_IN_RUSSIA = (By.LINK_TEXT, "Макдоналдс в России")
    CHARITY = (By.LINK_TEXT, "Благотворительность")
    FRANCHISING = (By.LINK_TEXT, "Франчайзинг")
    NEWS = (By.LINK_TEXT, "Новости")
    DELIVERY = (By.LINK_TEXT, "МакДоставка")

    FEEDBACK = (By.LINK_TEXT, "Обратная связь")
    FOR_MEDIA = (By.LINK_TEXT, "Для прессы")
    COOPERATION = (By.LINK_TEXT, "Сотрудничество")

    INSTAGRAM_ICON = (By.XPATH, "//a[@href = 'https://www.instagram.com/mcdonalds_rus/?hl=ru']")
    FACEBOOK_ICON = (By.XPATH, "//a[@href = 'https://www.facebook.com/mcdonaldsrussia/']")
    VK_ICON = (By.XPATH, "//a[@href = 'https://vk.com/mcdonaldsrussia']")
    YOUTUBE_ICON = (By.XPATH, "//a[@href = 'https://www.youtube.com/user/McDonaldsRussia']")
    VIBER_ICON = (By.XPATH, "//a[@href = 'viber://chat/?number=%2B79265221143']")
    WHATSAPP_ICON = (By.XPATH, "//a[@href = 'https://wa.me/%2B79265221143']")

    APP_STORE_BUTTON = (By.XPATH, "//a[@href = 'https://apps.apple.com/ru/app/макдоналдс/id896111038']")
    GOOGLE_PLAY_BUTTON = (By.XPATH, "//a[@href = 'https://play.google.com/store/apps/details?id=com.apegroup"
                                    ".mcdonaldsrussia&hl=ru']")
    APP_GALLERY_BUTTON = (By.XPATH, "//a[@href = 'https://appgallery.huawei.com/#/app/C102465481']")

    UNCHECKED_CHECKBOX = (By.CSS_SELECTOR, "span.el-checkbox__inner")
    CHECKED_CHECKBOX = (By.CSS_SELECTOR, "span.el-checkbox is-checked")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input.el-input__inner")
    SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, "div.subscribe__btn")

    SUCCESS_SUBSCRIPTION_TITLE = (By.CSS_SELECTOR, "span.subscribe__title")
    SUBSCRIBE_MORE_BUTTON = (By.CSS_SELECTOR, "div.subscribe__btn.subscribe__btn_more")

    @allure.step("Ввести email")
    def type_email(self, user_email):
        locator = self.EMAIL_FIELD
        try:
            email_field = WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.browser.save_screenshot("footer_exception.png")
            raise AssertionError("Элемент {} не найден на странице".format(locator))
        else:
            email_field.send_keys(user_email)







    # def is_title_present(self, title):
    #     element = self.browser.find_element(title)
    #     return element

