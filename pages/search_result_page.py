from appium.webdriver.common.appiumby import AppiumBy
import locators


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def click_search_field(self):
        self.driver.find_element(AppiumBy.ID, locators.SEARCH_FIELD_ID).click()

    def search_text(self, text):
        self.driver.find_element(AppiumBy.ID, locators.INPUT_FIELD_ID).send_keys(text)

    def clear_search_field(self):
        self.driver.find_element(AppiumBy.ID, locators.INPUT_FIELD_ID).clear()

    def search_results(self):
        return self.driver.find_elements(AppiumBy.XPATH, locators.RESULTS_XPATH)

    def click_back_button(self):
        self.driver.find_element(AppiumBy.XPATH, locators.BACK_BUTTON_XPATH).click()
