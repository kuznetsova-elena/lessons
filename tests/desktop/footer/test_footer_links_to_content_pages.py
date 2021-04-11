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
from page_objects.BasePage import BasePage


def test_link_work_at_mcdonalds(browser, url):
    page = BasePage(browser)
    page.click_link(FooterPage.WORK_IN_MCDONALDS)
    page_title = page.is_text_presented_on_page(WorkAtMcdonaldsPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{WorkAtMcdonaldsPage.URL}"
    assert "Присоединяйся к нашей команде!" == page_title


def test_link_mcdonalds_in_russia(browser, url):
    page_title = "Макдоналдс в России"
    page = BasePage(browser)
    page.click_link(FooterPage.MCDONALDS_IN_RUSSIA)
    text = page.is_text_presented_on_page(McdonaldsInRussiaPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{McdonaldsInRussiaPage.URL}"
    assert text == page_title


def test_link_charity(browser, url):
    page = BasePage(browser)
    page.click_link(FooterPage.CHARITY)
    page_title = page.is_text_presented_on_page(CharityPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{CharityPage.URL}"
    assert page_title == "МЫ ВЕРИМ, ЧТО У МАЛЕНЬКИХ ДЕТЕЙ НЕ ДОЛЖНО БЫТЬ БОЛЬШИХ ПРОБЛЕМ"


def test_link_franchising(browser, url):
    page_title = "Франчайзинг"
    page = BasePage(browser)
    page.click_link(FooterPage.FRANCHISING)
    text = page.is_text_presented_on_page(FranchisingPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{FranchisingPage.URL}"
    assert text == page_title


def test_link_news(browser, url):
    page_title = "Новости"
    page = BasePage(browser)
    page.click_link(FooterPage.NEWS)
    text = page.is_text_presented_on_page(NewsPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{NewsPage.URL}"
    assert text == page_title


def test_link_menu_delivery(browser, url):
    page_title = "МакДоставка"
    page = BasePage(browser)
    page.click_link(FooterPage.DELIVERY)
    text = page.is_text_presented_on_page(DeliveryPage.PAGE_TITLE).text
    assert browser.current_url == f"{url}{DeliveryPage.URL}"
    assert text == page_title


def test_link_feedback(browser, url):
    page_title = "Обратная связь"
    page = BasePage(browser)
    page.click_link(FooterPage.FEEDBACK)
    text = page.is_text_presented_on_page(FeedbackPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{FeedbackPage.URL}"
    assert text == page_title


def test_link_for_media(browser, url):
    page_title = "Для прессы"
    page = BasePage(browser)
    page.click_link(FooterPage.FOR_MEDIA)
    text = page.is_text_presented_on_page(ForMediaPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{ForMediaPage.URL}"
    assert text == page_title


def test_link_cooperation(browser, url):
    page_title = "Сотрудничество"
    page = BasePage(browser)
    page.click_link(FooterPage.COOPERATION)
    text = page.is_text_presented_on_page(CooperationPage.PAGE_TITLE).text

    assert browser.current_url == f"{url}{CooperationPage.URL}"
    assert text == page_title


