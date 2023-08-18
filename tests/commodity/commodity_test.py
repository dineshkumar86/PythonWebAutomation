import time
from pages.commodity.commodity import CommodityPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CommodityTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cop = CommodityPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_commodity_apis(self):
        self.cop.commodity_apis()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=2)
    def test_commodity_download(self):
        self.cop.commodity_download()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=3)
    def test_commodity_curency_change(self):
        self.cop.commodity_curency_change("INR")
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=4)
    def test_commodity_search(self):
        self.cop.commodity_search("Aluminum")
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=5)
    def test_commodity_chart_period(self):
        self.cop.commodity_chart_period()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))
