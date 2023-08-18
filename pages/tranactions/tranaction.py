import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class TranactionsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _tranaction_tab = "//li[contains(text(),'Transactions')]"
    _download_top_deal_makers = "//div[@class='my-2']//img[@src='/assets/img/excelDownload.png']"
    _download_deals_history = "//div[@class='col-1']//img[@src='/assets/img/excelDownload.png']"
    _PEVC_tab = "//li[@id='PEVCTab']"
    _download_PEVC_funding_summary = "//div[@class='col-3']//img[@src='/assets/img/excelDownload.png']"
    _download_PEVC_funding_details = "//div[@class='col-1 text-end custom-excel-icon pe-5']/img"
    _title = "//head//title"


    def tranaction_page(self):
        self.elementClick(self._tranaction_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    #        time.sleep(25)

    def download_top_deal_makers(self):
        self.tranaction_page()
        self.elementClick(self._download_top_deal_makers, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    #        time.sleep(3)

    def download_deals_history(self):
        self.tranaction_page()
        self.elementClick(self._download_deals_history, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    #        time.sleep(7)

    def PEVC_page(self):
        self.tranaction_page()
        self.elementClick(self._PEVC_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    #       time.sleep(20)

    def download_PEVC_funding_summary(self):
        self.PEVC_page()
        self.elementClick(self._download_PEVC_funding_summary, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    #        time.sleep(3)

    def download_PEVC_funding_details(self):
        self.PEVC_page()
        self.elementClick(self._download_PEVC_funding_details, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

#        time.sleep(7)






