from utilities.Custom_Logger import CustomLogger
from selenium.webdriver.support.select import Select
import logging
from snm_pages.pom_snm_loginpage import SNM_Login_Page
from snm_pages.pom_snm_homepage import SNM_HomePage
from snm_pages.pom_snm_tools_homepage import SNM_Tools_Homepage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from snm_pages.pom_snm_command_line import SNM_Tools_CommandLine
from utilities.test_data import UserData
import time
import inspect

class Util:
    cl = CustomLogger().custom_logger(logging.INFO)
    # driver = webdriver.Firefox()
    logindata = UserData("TestData", "logindata")
    ipdata = UserData("TestData", "IP")
    testData = UserData("TestData", "PMTestData")


    def take_screen_shot(self, methodname, driver):
        driver.save_screenshot("..\screenShots\\"+methodname+".png")

    def compare_titles(self, actual_title, expected_title):
        if actual_title == expected_title:
            self.cl.info("Title verified")
            return True
        else:
            self.cl.info("Title verification failed")
            return False

    def select_dropdown_by_text(self, webelement, text):
        sel = Select(webelement)
        sel.select_by_visible_text(text)

    def select_dropdown_by_index(self, webelement, index):
        sel = Select(webelement)
        sel.select_by_index(index)

    def select_dropdown_by_value(self, webelement, value):
        sel = Select(webelement)
        sel.select_by_value(value)

    def execute_command(self, driver, exeCmds):
        pmLink = self.ipdata.get_test_data(0,0)
        snmLink = self.ipdata.get_test_data(1,0)
        snmlogindata = self.logindata.parse_test_data("test_snm_valid_login", 1)
        pmTestData = self.testData.parse_test_data(inspect.stack()[1][3], 1)
        driver.get(snmLink)
        wait = WebDriverWait(driver, 10)
        lp = SNM_Login_Page(driver)
        hp = SNM_HomePage(driver)
        tp = SNM_Tools_Homepage(driver)
        cmdLine = SNM_Tools_CommandLine(driver)
        lp.snm_login(snmlogindata[0], snmlogindata[1])
        hp.click_tools()
        parentWindow = driver.current_window_handle
        tp.click_Command_Line()
        wait.until(ec.number_of_windows_to_be(2))
        ttlWindows = driver.window_handles
        for window in ttlWindows:
            if window != parentWindow:
                driver.switch_to_window(window)
                driver.switch_to_frame(cmdLine.get_commandFrame())
                for cmd in exeCmds:
                    cmdLine.set_command_filed_text_box(cmd)
                    cmdLine.click_command_apply_button()
                    time.sleep(1)
                driver.close()
        driver.switch_to_window(parentWindow)
        hp.click_logout()
        # driver.get(pmLink)








