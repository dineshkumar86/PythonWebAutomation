import time
from pages.tranactions.tranaction import TranactionsPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TranactionTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tp = TranactionsPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_tranaction(self):
        self.tp.tranaction_page()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=2)
    def test_download_top_deal_makers(self):
        self.tp.download_top_deal_makers()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=3)
    def test_download_deals_history(self):
        self.tp.download_deals_history()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=4)
    def test_PEVC(self):
        self.tp.PEVC_page()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=5)
    def test_download_PEVC_funding_summary(self):
        self.tp.download_PEVC_funding_summary()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=6)
    def test_download_PEVC_funding_details(self):
        self.tp.download_PEVC_funding_summary()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))
