import unittest
import pytest
from utilities.util import Util
import logging
from pages.pom_pm_user_page import PM_Users_Page
from pages.pom_login_page import PmLoginPage
from pages.pom_pm_homepage import PM_Home_Page
from utilities.Custom_Logger import CustomLogger
from utilities.util import Util
import time
import inspect


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


    def test_create_user(self):
        try:
            self.lp.login_in_to_pm("Arjuna", "Arjuna@12345")
            self.homepage.click_users()
            self.userpage.click_user_link()
            self.userpage.click_user_add_button()
            self.userpage.set_user_first_name("User100")
            self.userpage.set_user_last_name("User100")
            self.userpage.set_user_id("User100")
            self.homepage.wait_for_element(self.userpage.__user_password__, "name")
            self.userpage.set_user_password("User@100")
            self.userpage.set_user_confirm_password("User@100")
            self.cl.info("Entered password successfully")
            self.userpage.set_user_email_id("mitel@gmail.com")
            self.userpage.set_user_alternate_first_name("MitelUser")
            self.userpage.set_user_alternate_last_name("MitelLast")
            self.userpage.set_user__business1("My_Business")
            self.userpage.set_user__business2("My_business2")
            self.userpage.set_user_mobile1("+917975935256")
            self.userpage.set_user_mobile2("+918105855417")
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
# if __name__=="__main__":
#     unittest.main()