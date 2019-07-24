import unittest
import pytest
from utilities.delete_user_data import Delete_User_Data
import logging
from pages.pom_pm_user_page import PM_Users_Page
from pages.pom_login_page import PmLoginPage
from pages.pom_pm_homepage import PM_Home_Page
from utilities.Custom_Logger import CustomLogger
from utilities.util import Util
import time
import inspect
from utilities.test_data import UserData


@pytest.mark.usefixtures("setUp", "driver_unit")
class PM_User_Tests(unittest.TestCase):

    cl = CustomLogger().custom_logger(logging.INFO)
    sShot = Util()

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.userpage = PM_Users_Page(self.driver)
        self.lp = PmLoginPage(self.driver)
        self.homepage = PM_Home_Page(self.driver)
        self.util = Util()
        self.data = UserData("TestData", "logindata")
        self.delete = Delete_User_Data()


    def test_create_user(self):
        try:
            self.data.check_test_status(inspect.stack()[0][3])
            loginData = self.data.parse_test_data("test_pm_valid_login",1)
            userData = self.data.parse_test_data(inspect.stack()[0][3],1)
            self.lp.login_in_to_pm(loginData[0],loginData[1])
            self.homepage.click_users()
            self.userpage.click_user_link()
            self.userpage.click_user_add_button()
            self.userpage.set_user_first_name(userData[0])
            self.userpage.set_user_last_name(userData[0])
            self.userpage.set_user_id(userData[0])
            self.homepage.wait_for_element(self.userpage.__user_password__, "name")
            self.userpage.set_user_password(userData[1])
            self.userpage.set_user_confirm_password(userData[1])
            self.cl.info("Entered password successfully")
            self.userpage.set_user_email_id(userData[2])
            self.userpage.set_user_alternate_first_name(userData[3])
            self.userpage.set_user_alternate_last_name(userData[4])
            self.userpage.set_user__business1(userData[5])
            self.userpage.set_user__business2(userData[6])
            self.userpage.set_user_mobile1(userData[7])
            self.userpage.set_user_mobile2(userData[8])
            self.util.select_dropdown_by_index(self.userpage.get_user_department(), 0)
            self.userpage.click_user_select_department()
            self.userpage.click_user_apply_button()
            result = self.userpage.text_equals(self.userpage.get_user_add_actual_msg().text.strip(), self.userpage.__user_add_expected_msg__)
            self.assertTrue(result)
            self.userpage.click_user_done_button()
            self.cl.info("User added Successfully")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise
        finally:
            userData = self.data.parse_test_data(inspect.stack()[0][3], 1)
            self.delete.delete_data(self.userpage, self.driver, userData[0], self.sShot)
# if __name__=="__main__":
#     unittest.main()