import time
from pages.company.company import CompanyPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CompanyTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = CompanyPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_company(self):
        self.lp.company_page()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=2)
    def test_summary(self):
        self.lp.summary()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=3)
    def test_Financials(self):
        self.lp.Financials()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=4)
    def test_segInfo(self):
        self.lp.seg_info()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=5)
    def test_debtProfile(self):
        self.lp.debt_pro()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=6)
    def test_management(self):
        self.lp.management()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=7)
    def test_ownership(self):
        self.lp.ownership()
        result = self.ap.api_request()
        time.sleep(3)
        print("Result1: " + str(result))

    @pytest.mark.run(order=8)
    def test_AnalystCov(self):
        self.lp.Analyst_cov()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=9)
    def test_estimates_consensus(self):
        self.lp.estimates_consensus()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))


    @pytest.mark.run(order=10)
    def test_events(self):
        self.lp.events()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=11)
    def test_currency(self):
        self.lp.currency_conversion("USD")
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=12)
    def test_company_benchmark_period(self):
        self.lp.company_benchmark_period()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=13)
    def test_company_financials_period(self):
        self.lp.company_financials_period()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=14)
    def test_company_financials_expansion(self):
        self.lp.company_financials_expansion()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))


    @pytest.mark.run(order=15)
    def test_company_filings_period(self):
        self.lp.company_filings_period()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))


    @pytest.mark.run(order=15)
    def test_company_benchmark_edit(self):
        self.lp.company_benchmark_edit("bharat petroleum corp. ltd")
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))


