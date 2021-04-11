import pytest

from collections import namedtuple

from page_objects.desktop.WorkAtMcdonaldsPage import WorkAtMcdonaldsPage
from page_objects.desktop.McdonaldsInRussiaPage import McdonaldsInRussiaPage
from page_objects.desktop.CharityPage import CharityPage
from page_objects.desktop.FranchisingPage import FranchisingPage
from page_objects.desktop.NewsPage import NewsPage
from page_objects.desktop.DeliveryPage import DeliveryPage
from page_objects.desktop.FeedbackPage import FeedbackPage
from page_objects.desktop.ForMediaPage import ForMediaPage
from page_objects.desktop.CooperationPage import CooperationPage
from page_objects.desktop.FooterPage import FooterPage

TestData = namedtuple("TestData", ["footer_link", "page_title", "expected_url", "expected_title"])

data_list = [
    TestData(FooterPage.WORK_IN_MCDONALDS, WorkAtMcdonaldsPage.PAGE_TITLE, WorkAtMcdonaldsPage.URL, "Присоединяйся к нашей команде!"),
    TestData(FooterPage.MCDONALDS_IN_RUSSIA, McdonaldsInRussiaPage.PAGE_TITLE, McdonaldsInRussiaPage.URL, "Макдоналдс в России")
]

test_ids = [
    data_list[0].expected_title,
    data_list[1].expected_title,
]

@pytest.mark.parametrize("td", data_list, ids=test_ids)
def test_link_work_at_mcdonalds(browser, url, page, td):
    page.click_link(td.footer_link)
    page_title = page.is_text_presented_on_page(td.page_title).text

    assert browser.current_url == f"{url}{td.expected_url}"
    assert td.expected_title == page_title


def test_link_charity(browser, url, page):
    page.click_link(FooterPage.CHARITY)
    page_title = page.is_text_presented_on_page(CharityPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{CharityPage.URL}"
    assert page_title == "МЫ ВЕРИМ, ЧТО У МАЛЕНЬКИХ ДЕТЕЙ НЕ ДОЛЖНО БЫТЬ БОЛЬШИХ ПРОБЛЕМ"


def test_link_franchising(browser, url, page):
    page_title = "Франчайзинг"
    page.click_link(FooterPage.FRANCHISING)
    text = page.is_text_presented_on_page(FranchisingPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{FranchisingPage.URL}"
    assert text == page_title


def test_link_news(browser, url, page):
    page_title = "Новости"
    page.click_link(FooterPage.NEWS)
    text = page.is_text_presented_on_page(NewsPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{NewsPage.URL}"
    assert text == page_title


def test_link_menu_delivery(browser, url, page):
    page_title = "МакДоставка"
    page.click_link(FooterPage.DELIVERY)
    text = page.is_text_presented_on_page(DeliveryPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{DeliveryPage.URL}"
    assert text == page_title


def test_link_feedback(browser, url, page):
    page_title = "Обратная связь"
    page.click_link(FooterPage.FEEDBACK)
    text = page.is_text_presented_on_page(FeedbackPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{FeedbackPage.URL}"
    assert text == page_title


def test_link_for_media(browser, url, page):
    page_title = "Для прессы"
    page.click_link(FooterPage.FOR_MEDIA)
    text = page.is_text_presented_on_page(ForMediaPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{ForMediaPage.URL}"
    assert text == page_title


def test_link_cooperation(browser, url, page):
    page_title = "Сотрудничество"
    page.click_link(FooterPage.COOPERATION)
    text = page.is_text_presented_on_page(CooperationPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{CooperationPage.URL}"
    assert text == page_title


