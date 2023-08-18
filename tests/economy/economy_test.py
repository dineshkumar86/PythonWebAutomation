import time
from pages.economy.economy import EconomyPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class EconomyTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.dp = EconomyPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_economy_apis(self):
        self.dp.economy_apis()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=2)
    def test_economy_download(self):
        self.dp.economy_download()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=3)
    def test_economy_modify_country(self):
        self.dp.economy_modify_country("United States")
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=4)
    def test_economy_modify_chart(self):
        self.dp.economy_modify_chart()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))


