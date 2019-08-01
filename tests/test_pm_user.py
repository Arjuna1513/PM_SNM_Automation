import unittest
import pytest
from utilities.delete_user_data import Delete_User_Data
import logging
from pages.pom_pm_user_page import PM_Users_Page
from pages.pom_login_page import PmLoginPage
from utilities.Custom_Logger import CustomLogger
from utilities.util import Util
import inspect
from utilities.test_data import UserData
from utilities.naviagtion import Navigation
from pages.pom_pm_homepage import PM_Home_Page
from pages.pom_pm_extension import PM_Extension
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By
from utilities import util
import time


@pytest.mark.usefixtures("setUp", "driver_unit")
class PM_User_Tests(unittest.TestCase):

    cl = CustomLogger().custom_logger(logging.INFO)
    sShot = Util()

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.userpage = PM_Users_Page(self.driver)
        self.pmhomepage = PM_Home_Page(self.driver)
        self.lp = PmLoginPage(self.driver)
        self.homepage = PM_Home_Page(self.driver)
        self.util = Util()
        self.lgdata = UserData("TestData", "logindata")
        self.ipData = UserData("TestData", "IP")
        self.userdata = UserData("TestData", "PMTestData")
        self.delete = Delete_User_Data()
        self.navigate = Navigation()
        self.extpage = PM_Extension(self.driver)
        self.wait = WebDriverWait(self.driver,10)

    @pytest.mark.skip
    def test_create_user(self):
        try:
            self.driver.get(self.ipData.get_IP_data(0,0))
            self.userdata.check_test_status(inspect.stack()[0][3])
            loginData = self.lgdata.parse_test_data("test_pm_valid_login",1)
            userData = self.userdata.parse_test_data(inspect.stack()[0][3],1)
            self.lp.login_in_to_pm(loginData[0],loginData[1])
            self.homepage.click_users()
            self.userpage.click_user_link()
            self.userpage.click_user_add_button()
            self.userpage.set_user_first_name(userData[0])
            self.userpage.set_user_last_name(userData[0])
            self.userpage.set_user_id(userData[0])
            self.wait.until(ec.presence_of_element_located((By.NAME, self.userpage.__user_password__)))
            time.sleep(1)
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
            userData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
            self.delete.delete_data(self.pmhomepage, self.userpage, self.driver, userData[0], self.sShot)

    @pytest.mark.skip
    def test_edit_user(self):
        try:
            self.userdata.check_test_status(inspect.stack()[0][3])
            self.navigate.navigate_to_users_page(self.ipData, self.driver, self.lgdata, self.homepage,
                                                            self.userpage, self.sShot, self.lp)
            userData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
            self.cl.info("Before creating user")
            self.userpage.click_user_add_button()
            self.userpage.set_user_first_name(userData[0])
            self.userpage.set_user_last_name(userData[0])
            self.userpage.set_user_id(userData[0])
            self.wait.until(ec.presence_of_element_located((By.NAME, self.userpage.__user_password__)))
            time.sleep(1)
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
            self.cl.info("After user creation")
            self.cl.info("Let' search for the user")
            self.userpage.set_user_name_input_range(userData[0])
            self.userpage.click_user_view_button()
            self.userpage.element_click(
                "(//td[contains(text(),'"+userData[0]+"')])[1]//preceding-sibling::td[19]","xpath")
            self.userpage.get_element(self.userpage.__user_last_name__,"id").clear()
            self.userpage.set_user_last_name("Lastname")
            self.userpage.get_element(self.userpage.__user_email_id__,"id").clear()
            self.userpage.set_user_email_id("Lastname@gmail.com")
            self.userpage.click_user_apply_button()
            result = self.userpage.text_equals(self.userpage.get_user_change_actual_msg().text.strip(), self.userpage.__user_change_expected_msg__)
            self.assertTrue(result)
            self.userpage.click_user_done_button()
            self.cl.info("User edited Successfully")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise
        finally:
            userData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
            self.delete.delete_data(self.pmhomepage,self.userpage, self.driver, userData[0], self.sShot)

    @pytest.mark.skip
    def test_assign_extension_to_user(self):
        try:
            # self.navigate.navigate_to_users_page(self.ipData, self.driver, self.lgdata, self.userdata, self.homepage,
            #                                                 self.userpage, self.sShot, self.lp)
            self.userdata.check_test_status(inspect.stack()[0][3])
            userData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
            excCmds = []
            excCmds.append(userData[0])
            excCmds.append(userData[1])
            excCmds.append(userData[2])
            self.util.execute_command(self.driver,excCmds)
            self.navigate.navigate_to_users_page(self.ipData, self.driver, self.lgdata, self.homepage,
                                                            self.userpage, self.sShot, self.lp)
            print(userData)
            self.userpage.click_user_add_button()
            self.userpage.set_user_first_name(userData[3])
            self.userpage.set_user_last_name(userData[3])
            self.userpage.set_user_id(userData[3])
            # self.homepage.wait_for_element(self.userpage.__user_password__, "name")
            self.wait.until(ec.presence_of_element_located((By.NAME, self.userpage.__user_password__)))
            time.sleep(1)
            self.userpage.set_user_password(userData[4])
            self.userpage.set_user_confirm_password(userData[4])
            self.cl.info("Entered password successfully")
            time.sleep(1)
            self.userpage.set_user_email_id(userData[5])
            self.util.select_dropdown_by_index(self.userpage.get_user_department(), 0)
            self.userpage.click_user_select_department()
            self.userpage.click_user_next_button()
            self.userpage.set_user_existing_extension_input_field(userData[6])
            self.userpage.click_user_apply_button()
            result = self.userpage.text_equals(self.userpage.get_user_add_actual_msg().text.strip(), self.userpage.__user_add_expected_msg__)
            self.assertTrue(result)
            self.userpage.click_user_done_button()
            self.cl.info("User added Successfully")
            self.cl.info("After user creation")
            self.cl.info("Let' search for the user")
            self.userpage.set_user_name_input_range(userData[3])
            self.userpage.click_user_view_button()
            result = self.userpage.is_element_present(
                "(//td[contains(text(),'"+userData[6]+"')]//preceding-sibling::td[contains(text(),'"+userData[3]+"')])[1]", "xpath")
            if result:
                self.cl.info("User created with existing extension assigned")
        except:
            self.sShot.take_screen_shot(inspect.stack()[0][3], self.driver)
            raise
        finally:
            userData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
            # excCmds = []
            # excCmds.append(userData[7])
            # excCmds.append(userData[8])
            # excCmds.append(userData[9])
            # self.util.execute_command(self.driver,excCmds)
            self.delete.delete_data(self.pmhomepage,self.userpage, self.driver, userData[3], self.sShot)


    def test_no_users_found(self):
        self.userdata.check_test_status(inspect.stack()[0][3])
        testData = self.userdata.parse_test_data(inspect.stack()[0][3], 1)
        self.navigate.navigate_to_users_page(self.ipData, self.driver, self.lgdata, self.homepage,
                                                            self.userpage, self.sShot, self.lp)
        self.userpage.set_user_name_input_range(testData[0])
        self.userpage.click_user_view_button()
        result = self.userpage.text_equals(self.userpage.get_no_user_found_expected_message().text.strip(),self.userpage.get_no_user_found_actual_message().text.strip())
        assert result




# if __name__=="__main__":
#     unittest.main()