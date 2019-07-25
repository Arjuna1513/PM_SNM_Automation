from pages.pom_login_page import PmLoginPage
import time
import unittest
from utilities.Custom_Logger import CustomLogger
from utilities.util import Util
import logging
import pytest
import inspect
from utilities.test_data import UserData
from colorama import Fore, Style
from utilities.read_data import readCSVData
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setUp", "driver_unit")
class PM_Login_tests(unittest.TestCase):
    log = CustomLogger.custom_logger(logging.INFO)
    sShot = Util()

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = PmLoginPage(self.driver)
        self.data = UserData("TestData","logindata")


    # @data(*readCSVData("C:\\Users\\mallikar\\Documents\\Python_Workspace\\PM_SNM_Project\\testData.csv"))
    # @unpack
    @pytest.mark.run(order=4)
    def test_pm_valid_login(self):

        try:
            self.log.info("======Start of 'test_pm_valid_login' test======")
            self.data.check_test_status(inspect.stack()[0][3])
            dataList = self.data.parse_test_data(inspect.stack()[0][3],1)
            userName = dataList[0]
            userPwd = dataList[1]
            self.lp.login_in_to_pm(userName,userPwd)
            result = self.lp.pm_login_successful()
            assert result, "Login Un-Successful"
            time.sleep(3)
            self.log.info("======End of 'test_pm_valid_login' test======")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise


    @pytest.mark.run(order=1)
    def test_pm_invalidUserID_login(self):
        try:
            self.log.info("======Start of 'test_pm_invalidUserID_login' test======")
            self.data.check_test_status(inspect.stack()[0][3])
            dataList = self.data.parse_test_data(inspect.stack()[0][3])
            userName = dataList[0]
            userPwd = dataList[1]
            self.lp.login_in_to_pm(userName,userPwd)
            self.lp.pm_login_unsuccessful()
            self.log.info("Proper error message is displayed for invalid login")
            time.sleep(3)
            self.log.info("======End of 'test_pm_invalidUserID_login' test======")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise
        # driver.close()

    @pytest.mark.run(order=2)
    def test_pm_invalidPWD_login(self):
        try:
            self.log.info("======Start of 'test_pm_invalidPWD_login' test======")
            self.data.check_test_status(inspect.stack()[0][3])
            dataList = self.data.parse_test_data(inspect.stack()[0][3])
            userName = dataList[0]
            userPwd = dataList[1]
            self.lp.login_in_to_pm(userName,userPwd)
            self.lp.pm_login_unsuccessful()
            self.log.info("Proper error message is displayed for invalid login")
            time.sleep(3)
            self.log.info("======End of 'test_pm_invalidPWD_login' test======")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise

    @pytest.mark.run(order=3)
    def test_pmlogin_with_only_pwd(self):
        try:
            self.log.info("======Start of 'test_pmlogin_with_only_pwd' test======")
            self.data.check_test_status(inspect.stack()[0][3])
            dataList = self.data.parse_test_data(inspect.stack()[0][3])
            userPwd = dataList[0]
            self.lp.login_in_to_pm(pwd=userPwd)
            self.lp.pm_login_unsuccessful()
            self.log.info("Proper error message is displayed for invalid login")
            time.sleep(3)
            self.log.info("======End of 'test_pmlogin_with_only_pwd' test======")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise




"""Do not create an object and run any method and expect the pytest autouse to have
effect, becoz u r using pytest so do not create any object. U either run it from command
prompt or using run option."""