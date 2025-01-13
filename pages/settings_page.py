from appium.webdriver.common.appiumby import AppiumBy
import locators


class SettingsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_show_images_option(self):
        self.driver.find_element(AppiumBy.XPATH, locators.SHOW_IMAGES_XPATH).click()

    def click_show_link_previews_option(self):
        self.driver.find_element(AppiumBy.XPATH, locators.SHOW_LINK_PREVIEWS_XPATH).click()

    def click_send_usage_reports_option(self):
        self.driver.find_element(AppiumBy.XPATH, locators.SEND_USAGE_REPORTS_XPATH).click()

    def click_send_crash_reports_option(self):
        self.driver.find_element(AppiumBy.XPATH, locators.SEND_CRASH_REPORTS_XPATH).click()

    def navigate_home_page_button(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locators.NAVIGATE_HOME_PAGE_ACCESSIBILITY_ID).click()