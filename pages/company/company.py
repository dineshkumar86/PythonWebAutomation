import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class CompanyPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _company = "//li[contains(text(),'Company')]"
    _Summary_tab = "//button[contains(text(),'Summary')]"
    _download_commpany_profile = "//p[@id='companyStep7']"
    _close = "//button[contains(text(),'×')]"
    _img_stock_price_history_download = "//img[@id='companyStep9']"
    _financials_tab = "//button[@fragment='financials_tab']"
    _img_financials_download = "//img[@id='companyStep13']"
    _button_fin = "//button[contains(text(),'Download Excel')]"
    _segment_information = "//button[@class='btn'][1]"
    _img_segment_information_download = "//div[@id='segment_tab']//div[@class='col-4']/button[1]/img[1]"
    _debt_profile = "//button[@class='btn'][2]"
    _img_debt_profile_download = "//div[@id='debt_tab']//div[@class='col-4']/button[1]/img[1]"
    _tab_management = "//button[@class='btn'][3]"
    _img_management_key_employees = "//div[@id='management_tab']//div[@class='col-4']/button[1]/img[1]"
    _tab_owership = "//button[@class='btn'][4]"
    _img_ownership_downlaod = "//div[@id='ownership_tab']//div[@class='col-4']/img[1]"
    _tab_analyst_cov = "//button[@class='btn'][5]"
    _img_analyst_coverage = "//div[@id='analyst_tab']//div[@class='col-4']/img[1]"
    _img_estimates = "//div[@id='debt_tab']//div[@class='col-4 p-0']//img[1]"
    _estimates_period = "//div[@id='debt_tab']//div[@class='col-4 p-0']//div/button[contains(text(),'Quarter')]"
    _events = "//button[@class='btn'][6]"
    _img_events = "//div[@id='event_tab']//div[@class='col-4']//img[1]"
    _title = "//head//title"
    _currency = "//span[@id='select2-companyStep5-container']"
    _currency_box = "//body/span[1]/span[1]/span[1]/input[1]"
    _select_currency = "//li[contains(text(), 'USD')]"
    _benchmark_qtr = "//button[contains(text(),'Quarterly')]"
    _benchmark_yearly = "//button[contains(text(),'Yearly')]"
    _benchmark_edit = "//span[@class='fs12 edit_benchmark']"
    _select_benchmark_company = "//span[@id='select2-companyDropdownMNAbenchmark-container']"
    _remove_benchmark_company = "//tbody/tr[2]/td[1]/span[1]/i[1]"
    _input_benchmark_company = "//body/span[1]/span[1]/span[1]/input[1]"
    _select_bench_company = "//ul[@id='select2-companyDropdownMNAbenchmark-results']//li[1]"
    _financials_dropdown = "//div[@id='companyStep11']//span[1]/span[1]/span[1]/span[1]"
    _select_LTM = "//li[contains(text(),'LTM')]"
    _fin_expansion_button = "//button[@id='companyStep12']"
    _fin_BS = "//button[contains(text(),'Balance Sheet')]"
    _fin_expan_annual = "//span[contains(text(),'Annual')]"
    _fin_expan_qtr = "//li[contains(text(),'Quarter')]"
    _fin_expan_semi_annual = "//li[contains(text(),'Semi-Annual')]"
    _fin_expan_annual_with_interim = "//li[contains(text(),'Annual with interim')]"
    _fin_expan_qtr_box = "//span[contains(text(),'Quarter')]"
    _fin_expan_semi_box = "//span[contains(text(),'Semi-Annual')]"
    _fin_expan_LTM_box = "//span[contains(text(),'LTM')]"
    _tab_filings = "//button[contains(text(),'Filings')]"
    _company_filings = "//span[@id='select2-companyStep17-container']"
    _company_filings_dropdown = "//ul[@id='select2-companyStep17-results']/li[{}]"

    def company_page(self):
        self.elementClick(self._company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def summary(self):
        self.elementClick(self._Summary_tab, locatorType="xpath")
        self.elementClick(self._download_commpany_profile, locatorType="xpath")
        time.sleep(3)
        self.elementClick(self._close, locatorType="xpath")
        self.elementClick(self._img_stock_price_history_download, locatorType="xpath")
        time.sleep(3)

    def Financials(self):
        self.elementClick(self._financials_tab, locatorType="xpath")
        self.elementClick(self._img_financials_download, locatorType="xpath")
        self.elementClick(self._button_fin, locatorType="xpath")
        time.sleep(3)

    def seg_info(self):
        self.elementClick(self._segment_information, locatorType="xpath")
        self.elementClick(self._img_segment_information_download, locatorType="xpath")

    def debt_pro(self):
        self.elementClick(self._debt_profile, locatorType="xpath")
        self.elementClick(self._img_debt_profile_download, locatorType="xpath")

    def management(self):
        self.elementClick(self._tab_management, locatorType="xpath")
        self.elementClick(self._img_management_key_employees, locatorType="xpath")

    def ownership(self):
        self.elementClick(self._tab_owership, locatorType="xpath")
        self.elementClick(self._img_ownership_downlaod, locatorType="xpath")

    def Analyst_cov(self):
        self.elementClick(self._tab_analyst_cov, locatorType="xpath")
        self.elementClick(self._img_analyst_coverage, locatorType="xpath")

    def estimates_consensus(self):
        self.elementClick(self._tab_analyst_cov, locatorType="xpath")
        self.elementClick(self._img_estimates, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._estimates_period, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def events(self):
        self.elementClick(self._events, locatorType="xpath")
        self.elementClick(self._img_events, locatorType="xpath")

    def currency_conversion(self, currency):
        self.elementClick(self._Summary_tab, locatorType="xpath")
        self.elementClick(self._currency, locatorType="xpath")
        self.sendKeys(currency, self._currency_box, locatorType="xpath")
        self.elementClick(self._select_currency, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def company_benchmark_period(self):
        self.elementClick(self._Summary_tab, locatorType="xpath")
        self.elementClick(self._benchmark_qtr, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._benchmark_yearly, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def company_benchmark_edit(self, company):
        self.elementClick(self._benchmark_edit, locatorType="xpath")
        self.elementClick(self._remove_benchmark_company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._select_benchmark_company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.sendKeys(company, self._input_benchmark_company, locatorType="xpath")
        self.elementClick(self._select_bench_company, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)


    def company_financials_period(self):
        self.elementClick(self._financials_tab, locatorType="xpath")
        self.elementClick(self._financials_dropdown, locatorType="xpath")
        self.elementClick(self._select_LTM, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def company_financials_expansion(self):
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._financials_tab, locatorType="xpath")
        self.elementClick(self._fin_expansion_button, locatorType="xpath")
        self.WindowHandle(window=1)
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._fin_expan_annual, locatorType="xpath")
        self.elementClick(self._fin_expan_qtr, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._fin_expan_qtr_box, locatorType="xpath")
        self.elementClick(self._fin_expan_semi_annual, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)
        self.elementClick(self._fin_expan_semi_box, locatorType="xpath")
        self.elementClick(self._select_LTM, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

        self.elementClick(self._fin_expan_LTM_box, locatorType="xpath")
        self.elementClick(self._fin_expan_annual_with_interim, locatorType="xpath")
        userSettingsElement = self.waitForElement(locator=self._title,
                                                  locatorType="xpath", pollFrequency=1)

    def company_filings_period(self):
        self.elementClick(self._tab_filings, locatorType="xpath")
        for filings in range(1, 5):
            self.elementClick(self._company_filings, locatorType="xpath")
            self.elementClick(self._company_filings_dropdown.format(filings), locatorType="xpath")
            userSettingsElement = self.waitForElement(locator=self._title,
                                                      locatorType="xpath", pollFrequency=1)
