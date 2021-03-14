import pytest
import time
from page_objects.desktop.MainPage import MainPage


@pytest.mark.smoke
@pytest.mark.authorization
def test_add_to_cart(browser):
    time.sleep(3)
    assert False
    # main_page = MainPage(browser)
    # main_page.click_product(product)
    # main_page.add_to_cart()
    # main_page.open_cart()
    # assert main_page.is_element_present(CartLocators.TITLE)
