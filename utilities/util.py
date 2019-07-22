from  utilities.Custom_Logger import CustomLogger
from selenium.webdriver.support.select import Select
import logging
class Util:
    cl = CustomLogger().custom_logger(logging.INFO)

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

