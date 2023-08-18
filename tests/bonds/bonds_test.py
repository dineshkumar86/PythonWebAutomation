import time
from pages.bonds.bonds import BondsPage
from pages.apiRequest import api
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BondsTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.bp = BondsPage(self.driver)
        self.ap = api(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_bonds(self):
        self.bp.bonds_page()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=2)
    def test_bonds_list(self):
        self.bp.bonds_list()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=3)
    def test_bonds_comparable_edit(self):
        self.bp.bonds_comparable_edit()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

    @pytest.mark.run(order=4)
    def test_bonds_advanced_search(self):
        self.bp.bonds_advanced_search()
        result = self.ap.api_request()
        time.sleep(3)
        assert result == True
        print("Result1: " + str(result))

