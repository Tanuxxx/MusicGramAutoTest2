import pytest
import os
import allure

from appium import webdriver

class Test:

    @classmethod
    def setup(cls):
        cls.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'iOS',
                'platformVersion': '9.3.2',
                'deviceName': "Provectus iPhone 6S",
                'udid': "4a229109c6e0979665efc7f934fb743aaefb37a3",
                "noReset": "false",
                "automationName": "xcuitest",
                "appiumVersion": "1.6.1-beta",
                "browser": "safari"
            })

        cls.driver.implicitly_wait(300)
        #cls.driver.switch_to.alert.accept()


    @allure.feature('Open browser')
    @allure.story('Browser')
    def test_open_browser(cls):
        cls.driver.get("http://www.google.com")

