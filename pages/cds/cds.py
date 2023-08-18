import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CdsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cdsTab = "//li[contains(text(),'CDS')]"
    _title = "//head//title"
    _select_sector = "//span[contains(text(),'Select Sector')]"
    _select_sector_list = "//span[@class='select2-results']//ul/li[{}]"
    _select_currency = "//span[contains(text(),'Select Currency')]"
    _select_currency_list = "//span[@class='select2-results']//ul/li[{}]"
    _select_cds = "//span[contains(text(),'Select CDS')]"
    _select_cds_list = "//span[@class='select2-results']//ul/li[{}]"
    _edit = "//span[@class='editbtn-fi editbtn-cds']"
    _remove_cds = "//tbody/tr[2]/td[1]/div[1]/span[1]/i[1]"
    _select_cds_drop = "//span[@id='select2-comaparablesSearch-container']"
    _select_cds_list_1 = "//span[@class='select2-results']//ul/li[1]"
    _reset = "//span[@class='reset']"
    _advanced_search = "//span[contains(text(),'ADVANCED SEARCH')]"
    _advanced_search_company = "//tbody/tr[1]/td[1]/a"

    def cds_page(self):
        self.elementClick(self._cdsTab, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def cds_list(self):
        self.cds_page()
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        for cds in range(2, 5):
            self.elementClick(self._select_sector, locatorType="xpath")
            self.elementClick(self._select_sector_list.format(cds), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_currency, locatorType="xpath")
            self.elementClick(self._select_currency_list.format(cds), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_cds, locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_cds_list.format(cds), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)

    def cds_comparable_edit(self):
        self.cds_page()
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._edit, locatorType="xpath")
        self.elementClick(self._remove_cds, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._select_cds_drop, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_cds_list_1, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._reset, locatorType="xpath")

    def bonds_advanced_search(self):
        self.cds_page()
        self.elementClick(self._advanced_search, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._advanced_search_company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
