import time
from pages.derivatives.derivatives import DerivativesPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DerivativesTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.dp = DerivativesPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_derivatives(self):
        self.dp.derivatives_page()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

