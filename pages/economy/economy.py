import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class EconomyPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _economy_tab = "//li[contains(text(),'Economy')]"
    _download_economy = "//img[@src='/assets/img/excelDownload.png']"
    _title = "//head//title"
    _select_country = "//span[contains(text(),'Select Country')]"
    _country = "//body/span[1]/span[1]/span[1]/input[1]"
    _select_country_list = "//span[@class='select2-results']/ul/li"
    _select_gdp = "//span//span[contains(text(),'GDP Annual Growth Rate (Quarterly)')]"
    _select_gdp_list = "//span[@class='select2-results']/ul/li[1]"

    def economy_apis(self):
        self.elementClick(self._economy_tab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def economy_download(self):
        self.economy_apis()
        self.elementClick(self._download_economy, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def economy_modify_country(self,country):
        self.economy_apis()
        self.elementClick(self._select_country, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.sendKeys(country,self._country,locatorType="xpath")
        self.elementClick(self._select_country_list, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def economy_modify_chart(self):
        self.economy_apis()
        self.elementClick(self._select_gdp, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_gdp_list, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)





