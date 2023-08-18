import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CommodityPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _commodity_tab = "//li[contains(text(),'Commodity')]"
    _download_commodity = "//img[@src='/assets/img/excelDownload.png']"
    _title = "//head//title"
    _select_currency = "//span//span[contains(text(),'Select Currency')]"
    _currency_input = "//body/span[1]/span[1]/span[1]/input[1]"
    _select_currency_list = "//span[@class='select2-results']/ul/li"
    _select_commodity = "//div[@id='commodityStep1']//span//span[@class='selection']/span[1]"
    _commodity_period = "//ul[@id='commodityStep2']/li[{}]"

    def commodity_apis(self):
        self.elementClick(self._commodity_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def commodity_download(self):
        self.commodity_apis()
        self.elementClick(self._download_commodity, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def commodity_curency_change(self,currency):
        self.commodity_apis()
        self.elementClick(self._select_currency, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.sendKeys(currency, self._currency_input, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_currency_list, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def commodity_search(self,commodity):
        self.commodity_apis()
        self.elementClick(self._select_commodity, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.sendKeys(commodity, self._currency_input, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_currency_list, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def commodity_chart_period(self):
        self.commodity_apis()
        for commodity in range(1,7):
            self.elementClick(self._commodity_period.format(commodity), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)