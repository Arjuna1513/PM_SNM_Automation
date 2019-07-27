# import selenium
# import unittest
from base.selenium_driver import SeleniumDriver
class PM_Home_Page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __users__ = "Users"
    __services__ = "Services"
    __administrators__ = "Administrators"
    __system__ = "System"
    __logs__ = "Logs"
    __ownSettings__ = "Own_Settings"

    def get_users(self):
        return self.get_element(self.__users__, "id")

    def get_services(self):
        return self.get_element(self.__services__, "id")

    def get_administrators(self):
        return self.get_element(self.__administrators__, "id")

    def get_system(self):
        return self.get_element(self.__system__, "id")

    def get_logs(self):
        return self.get_element(self.__logs__, "id")

    def get_own_settings(self):
        return self.get_element(self.__ownSettings__, "id")

    def click_users(self):
        self.element_click(self.__users__, "id")

    def click_services(self):
        self.element_click(self.__services__, "id")

    def click_administrators(self):
        self.element_click(self.__administrators__, "id")

    def click_system(self):
        self.element_click(self.__system__, "id")

    def click_logs(self):
        self.element_click(self.__logs__, "id")

    def click_own_settings(self):
        self.element_click(self.__ownSettings__, "id")