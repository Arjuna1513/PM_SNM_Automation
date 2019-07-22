import unittest
from tests.pm_login_tests import PM_Login_tests
from tests.pm_user_tests import PM_User_Tests

cl1 = unittest.TestLoader().loadTestsFromTestCase(PM_Login_tests)
cl2 = unittest.TestLoader().loadTestsFromTestCase(PM_User_Tests)

sanity_suite = unittest.TestSuite([cl1, cl2])
unittest.TextTestRunner().run(sanity_suite)
