from base.selenium_driver import SeleniumDriver
from utilities.Custom_Logger import CustomLogger
import logging


class PmLoginPage(SeleniumDriver):
    log = CustomLogger.custom_logger(logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __PMlogin_user_id__ = "userId"
    __PMlogin_user_pwd__ = "password"
    __PMlogin_submit_button__ = "login"
    __pmlogin_failure_message__ = "The user or password is incorrect. Please try again."


    # def getPMLoginUserIdField(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_user_id__)
    def getPMLoginUserIdField(self):
       return self.get_element(self.__PMlogin_user_id__, "name")

    # def getPMUserPwdField(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_user_pwd__)
    def getPMUserPwdField(self):
        return self.get_element(self.__PMlogin_user_pwd__, "name")

    # def getLoginSubmitButton(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_submit_button__)
    def getLoginSubmitButton(self):
        return self.get_element(self.__PMlogin_submit_button__, "name")

    # def setPMLoginUserID(self, userName):
    #     self.getPMLoginUserIdField().send_keys(userName)
    def setPMLoginUserID(self, userName):
        self.sendKeys(userName, self.__PMlogin_user_id__, "name")

    # def setPmUserPwdField(self, pwd):
    #     self.getPMUserPwdField().send_keys(pwd)
    def setPmUserPwdField(self, pwd):
        self.sendKeys(pwd, self.__PMlogin_user_pwd__,"name")

    # def clickPMUserLoginSubmitButton(self):
    #     self.getLoginSubmitButton().click()
    def clickPMUserLoginSubmitButton(self):
        self.element_click(self.__PMlogin_submit_button__, "name")

    def login_in_to_pm(self, userid="", pwd=""):
        self.setPMLoginUserID(userid)
        self.getPMUserPwdField().click()
        self.setPmUserPwdField(pwd)
        self.clickPMUserLoginSubmitButton()
        # assert self.driver.find_element(By.XPATH,
        #                                 "//a/b[contains(text(), 'Logout')]").is_enabled(), "Login is Not Successful"

    def pm_login_successful(self):
        return self.is_element_present("//a/b[contains(text(), 'Logout')]", "xpath")

    def pm_login_unsuccessful(self):
        element = self.get_element("error","class")
        assert element.text.strip()==self.__pmlogin_failure_message__, "No proper error message"


    """
    The below code is general page object model but we can still customize it better to
    make the framework better...
    """

    # def getPMLoginUserIdField(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_user_id__)
    #
    # def getPMUserPwdField(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_user_pwd__)
    #
    # def getLoginSubmitButton(self):
    #     return self.driver.find_element(By.NAME, self.__PMlogin_submit_button__)
    #
    # def setPMLoginUserID(self, userName):
    #     self.getPMLoginUserIdField().send_keys(userName)
    #
    # def setPmUserPwdField(self, pwd):
    #     self.getPMUserPwdField().send_keys(pwd)
    #
    # def clickPMUserLoginSubmitButton(self):
    #     self.getLoginSubmitButton().click()