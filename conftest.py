from appium import webdriver
from appium.options.android import UiAutomator2Options


def start_driver():
    options = UiAutomator2Options()
    options.automation_name = "UiAutomator2"
    options.platform_name = "Android"
    options.platform_version = "12"
    options.device_name = "Android Device"
    options.udid = "RF8M20R1QCB"
    options.autoGrantPermissions = True
    options.app_package = "org.wikipedia.alpha"
    options.app_activity = "org.wikipedia.main.MainActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
