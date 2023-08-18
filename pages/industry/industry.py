import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class IndustryPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _industry_tab = "//li[contains(text(),'Industry')]"
    _title = "//head//title"


    def industry_page(self):
        self.elementClick(self._industry_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)



