# from selenium import webdriver
# import unittest
from base.selenium_driver import SeleniumDriver
# from selenium.webdriver.common.by import By
class PM_Services_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Extension = "Extension"  #id
    __Available_Extensions = "Available_Extensions"  #id
    __Individual_Diversion = "Individual_Diversion"  #id
    __Mailbox = "Mailbox"  #id


    def click_Extensions_tab(self):
        self.element_click(self.__Extension, "id")

    def click_Available_Extensions_tab(self):
        self.element_click(self.__Available_Extensions, "id")

    def click_Individual_Diversion_tab(self):
        self.element_click(self.__Individual_Diversion, "id")

    def click_Mailbox_tab(self):
        self.element_click(self.__Mailbox, "id")