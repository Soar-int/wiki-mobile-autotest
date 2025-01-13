import time
import conftest
from pages.home_page import HomePage
from pages.search_result_page import SearchPage
from pages.settings_page import SettingsPage


def test_home_page_navigation():
    driver = conftest.start_driver()
    home_page = HomePage(driver)
    home_page.scroll_down()
    home_page.navigate_my_list()
    time.sleep(3)
    home_page.navigate_history()
    time.sleep(3)
    home_page.navigate_nearby()
    time.sleep(3)
    home_page.navigate_explore()
    time.sleep(3)
    home_page.scroll_up()


def test_search_field():
    driver = conftest.start_driver()
    driver.implicitly_wait(5)
    search_page = SearchPage(driver)
    search_page.click_search_field()
    search_page.search_text("New York")
    results = search_page.search_results()
    for i in results:
        assert "New York" in i.text
    search_page.clear_search_field()

    search_page.click_back_button()


def test_disable_options_from_settings():
    driver = conftest.start_driver()
    driver.implicitly_wait(5)
    settings_page = SettingsPage(driver)
    home_page = HomePage(driver)
    home_page.click_settings_button()
    home_page.select_settings()
    settings_page.click_show_images_option()
    settings_page.click_show_link_previews_option()
    settings_page.click_send_usage_reports_option()
    settings_page.click_send_crash_reports_option()
    settings_page.navigate_home_page_button()
