from page_objects.MainPage import MainPage
from page_objects.locators import MainPageLocators, CartLocators


def test_add_to_cart(browser):
    product = MainPageLocators.PRODUCT_SNIPPET
    page = MainPage(browser)

    page.load(MainPageLocators.URL)
    page.click_product(product)
    page.add_to_cart()
    page.open_cart()
    assert page.is_element_present(CartLocators.TITLE)
