import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class DerivativesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _derivatives_tab = "//li[contains(text(),'Derivatives')]"
    _title = "//head//title"


    def derivatives_page(self):
        self.elementClick(self._derivatives_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)



