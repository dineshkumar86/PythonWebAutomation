import unittest
from tests.home.login_tests import LoginTests
from tests.company.company_test import CompanyTests
from tests.cds.cds_test import CdsTests
from tests.bonds.bonds_test import BondsTests
from tests.derivatives.derivatives_test import DerivativesTests
from tests.commodity.commodity_test import CommodityTests
from tests.industry.industry_test import IndustryTests
from tests.tranaction.tranaction_test import TranactionTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CompanyTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CdsTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(BondsTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CommodityTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(IndustryTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(TranactionTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(DerivativesTests)


# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8])

unittest.TextTestRunner(verbosity=2).run(smokeTest)