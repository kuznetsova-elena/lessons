from selenium.webdriver.common.by import By


class Footer:
    ABOUT_US_TITLE = (By.XPATH, "//div/span[contains(., 'О нас')]")
    CONTACTS_TITLE = (By.XPATH, "//div/span[contains(., 'Контакты')]")
    SUBSCRIBE_TITLE = (By.XPATH, "//div/span[contains(., 'Подписывайтесь на рассылку')]")
    WORK_IN_MCDONALDS = (By.LINK_TEXT, "Работа в Макдоналдс")
    # WORK_IN_MCDONALDS = (By.LINK_TEXT, 'Работа в Макдоналдс')
    # WORK_IN_MCDONALDS = (By.LINK_TEXT, 'Работа в Макдоналдс')
    # WORK_IN_MCDONALDS = (By.LINK_TEXT, 'Работа в Макдоналдс')
    # WORK_IN_MCDONALDS = (By.LINK_TEXT, 'Работа в Макдоналдс')


class MainPageLocators:
    URL = "https://mcdonalds.ru"
    BANNER_SLIDER = (By.CSS_SELECTOR, "div.base-slider__wrap.swiper-wrapper > div:nth-child(1)")
    OPEN_CART_BUTTON = (By.CSS_SELECTOR, "span.mini-cart__price")
    PRODUCT_SNIPPET = (By.CSS_SELECTOR, "ul.menu-catalog > li:nth-child(1)")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "div.base-modal__body>div>div>div>div>div>div:nth-child(2)>button>span")


class CartLocators:
    TITLE = (By.CLASS_NAME, 'cart-drawer__header')
    CLEAR_BUTTON = (By.CSS_SELECTOR, 'button[text="Очистить"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[class="el-drawer__close-btn"]')
#__layout > div > header > div > div.page-header__wrap.page-header__wrap_bottom-border > div.page-header__content > div.page-header__top > div > button