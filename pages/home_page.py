from appium.webdriver.common.appiumby import AppiumBy
import locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self):
        self.driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=1, duration=1000)

    def scroll_up(self):
        self.driver.swipe(start_x=500, start_y=500, end_x=500, end_y=1500, duration=1000)

    def navigate_explore(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locators.EXPLORE_ACCESSIBILITY_ID).click()

    def navigate_my_list(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locators.MY_LIST_ACCESSIBILITY_ID).click()

    def navigate_history(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locators.HISTORY_ACCESSIBILITY_ID).click()

    def navigate_nearby(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locators.NEARBY_ACCESSIBILITY_ID).click()

    def click_search_field(self):
        self.driver.find_element(AppiumBy.ID, locators.SEARCH_FIELD_ID).click()

    def click_settings_button(self):
        self.driver.find_element(AppiumBy.ID, locators.SETTINGS_BUTTON_ID).click()

    def select_settings(self):
        self.driver.find_element(AppiumBy.ID, locators.SELECT_SETTINGS_ID).click()


