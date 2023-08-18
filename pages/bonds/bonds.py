import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class BondsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _bondTab = "//li[contains(text(),'Bonds')]"
    _select_category = "//span[contains(text(),'Select Category')]"
    _select_category_list = "//span[@class='select2-results']//ul/li[{}]"
    _select_currency = "//span[contains(text(),'Select Currency')]"
    _select_currency_list = "//span[@class='select2-results']//ul/li[{}]"
    _select_bond = "//span[contains(text(),'Select Bond')]"
    _select_bond_list = "//span[@class='select2-results']//ul/li[{}]"
    _chart_drop_down = "//span//span[contains(text(),'Price')]"
    _chart_drop_down_list = "//span[@class='select2-results']//ul/li[2]"
    _title = "//head//title"
    _edit = "//span[@class='editbtn-fi editbtn-cds']"
    _remove_security = "//tbody/tr[2]/td[1]/div[1]/span[1]/i[1]"
    _select_security = "//span//span[contains(text(),'Select Security')]"
    _select_security_list = "//span[@class='select2-results']//ul/li[1]"
    _reset = "//span[@class='reset']"
    _advanced_search = "//span[contains(text(),'ADVANCED SEARCH')]"
    _advanced_search_company = "//tbody/tr[1]/td[1]/a"


    def bonds_page(self):
        self.elementClick(self._bondTab, locatorType="xpath")
        time.sleep(3)

    def bonds_list(self):
        self.bonds_page()
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        for bond in range(1,5):
            self.elementClick(self._select_category, locatorType="xpath")
            self.elementClick(self._select_category_list.format(bond), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_currency, locatorType="xpath")
            self.elementClick(self._select_currency_list.format(bond), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_bond, locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._select_bond_list.format(bond), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
            self.elementClick(self._chart_drop_down, locatorType="xpath")
            self.elementClick(self._chart_drop_down_list, locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)


    def bonds_comparable_edit(self):
        self.bonds_page()
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._edit, locatorType="xpath")
        self.elementClick(self._remove_security, locatorType="xpath")
        self.elementClick(self._select_security, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_security_list, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._reset, locatorType="xpath")

    def bonds_advanced_search(self):
        self.bonds_page()
        self.elementClick(self._advanced_search, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._advanced_search_company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)





