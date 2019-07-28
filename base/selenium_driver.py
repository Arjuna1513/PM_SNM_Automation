from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from utilities.Custom_Logger import CustomLogger
import logging
from selenium import webdriver
# from utilities.util import Util


class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver
    cl = CustomLogger().custom_logger(logging.INFO)

    def gettype(self, locatortype):
        locatortype = locatortype.lower()
        if locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "link":
            return By.LINK_TEXT
        elif locatortype == "class":
            return By.CLASS_NAME
        elif locatortype == "partialink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.cl.info("Invalid locator type")
        return False

    # def getElement(self, locator, locatorType):
    #     element = None
    #     try:
    #         byType = self.getType(locatorType)
    #         # print(type(byType))
    #         element = self.driver.find_element(byType, locator)
    #         # print(f"Element value is {element}")
    #         if element is not None:
    #             print("Element Found")
    #             return element
    #         else:
    #             print("Print element Not Found")
    #     except:
    #         print("Element Not Found")
    #     return element
    def get_element(self, locator, locatortype):
        locatorType = locatortype.lower()
        bytype = self.gettype(locatortype)
        element = self.driver.find_element(bytype, locator)
        if element is not None:
            self.cl.info(f"Element with the given locator '{locator}' and "
                         f"locator type '{locatortype}' is found ")
            return element
        else:
            self.cl.info(f"Element with the given locator '{locator}' and "
                         f"locator type '{locatortype}' is not found ")
        return element

    def get_elementsList(self, locator, locatortype):
        locatortype = locatortype.lower()
        by_type = self.gettype(locatortype)
        list1 = self.driver.find_elements(by_type, locator)
        if list1 is not None:
            self.cl.info(f"List with the locator '{locator}' and locatortype '{locatortype}' is found")
            return list1
        else:
            self.cl.info(f"List with the locator '{locator}' and locatortype '{locatortype}' is not found")

    def sendKeys(self, value, locator, locatortype):
        try:
            element = self.get_element(locator, locatortype)
            element.send_keys(value)
            self.cl.info(f"data has been entered in the '{locator}' with the locator type '{locatortype}'")
        except:
            self.cl.info(f"Cannot send data to the "
                         f"element with locator '{locator}' and the locator type '{locatortype}'")

    def element_click(self, locator, locatortype):
        try:
            element = self.get_element(locator, locatortype)
            element.click()
            self.cl.info(f"Clicked on the element with "
                         f"locator '{locator}' and locator-type '{locatortype}'")
        except:
            self.cl.info(f"Cannot click on the element with the "
                         f"locator '{locator}' and locator-type '{locatortype}'")

    def is_element_present(self, locator, locatortype):
        try:
            bytype = self.gettype(locatortype)
            element = self.driver.find_element(bytype, locator)
            if element is not None:
                self.cl.info("Element is Found")
                return True
            else:
                self.cl.info("Element Not Found")
                return False
        except:
            self.cl.info("Element Not Found")
        return False

    def elements_presence_check(self, locator, locatortype):
        try:
            bytype = self.gettype(locatortype)
            list1 = self.driver.find_elements(bytype, locator)
            if len(list1) > 0:
                self.cl.info(f"Element is Found")
                return True
            else:
                self.cl.info("Element Not Found")
                return False
        except:
            self.cl.info("Element Not Found")
        return False

    def wait_for_element(self, locator, locatortype):
        element = None
        try:
            bytype = self.gettype(locatortype)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1)
            element = wait.until(ec.element_to_be_clickable((bytype, locator)))
            if element is not None:
                self.cl.info(f"Waited till the Element is present and is click-able")
                return element
        except:
            self.cl.info(f"Waited for the element to be click-able but failed.")
        return element

    # def verify_title(self, expected_title):
    #     actual_title = self.driver.title
    #     return Util().compare_titles(actual_title, expected_title)

    def get_text(self, locator, locatortype):
        element = self.get_element(locator, locatortype)
        if element is not None:
            return element.text
        else:
            self.cl.info(f"Could not find the "
                         f"element with locator '{locator}' and locatortype '{locatortype}'")

    def scrollBrowser(self, value, scrollDir):
        scrollDir = scrollDir.lower()
        if scrollDir == "up":
            self.driver.execute_script("window.scrollBy(0, "+-value+")")
        elif scrollDir == "down":
            self.driver.execute_script("window.scrollBy(0, "+value+")")

    def text_equals(self, expected, actual):
        if expected == actual:
            return True
        else:
            return False
    #
    # def take_screen_shot(self, methodName):
    #     self.driver.save_screenshot("..\screenShots\\"+methodName+".png")
