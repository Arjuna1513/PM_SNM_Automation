from selenium import webdriver
import unittest
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.by import By
class PM_Users_Page(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __user__ = "User"
    __user_add_button__ = "onAddButton" #name
    __user_name_input_range__ = "range" #name
    __user_view_button__ = "onViewRangeButton" #name
    __user_next_button__ = "onNextButtonTopID" #id
    __user_apply_button__ = "onApplyButtonTopID" #id
    __user_cancel_button__ = "(//input[@name='onCancelButton'])[1]" #xpath
    __user_first_name__ = "myUser_VO.firstName" #id
    __user_last_name__ = "myUser_VO.lastName" #id
    __user_user_id__ = "myUser_VO.userId" #id
    __user_password__ = "myUser_VO.password" #name
    __user_confirm_password__ = "confirmPassword" #name
    __user_email_id__ = "myUser_VO.email" #id
    __user_alternate_first_name__ = "myAltFirstNames" #id
    __user_alternate_last_name__ = "myAltLastNames"
    __user__business1__ = "mySelectedUDFList[0]" #id
    __user__business2__ = "mySelectedUDFList[1]"  # id
    __user_mobile1__ = "mySelectedUDFList[2]" #id
    __user_mobile2__ = "mySelectedUDFList[3]"
    __user_department__ = "mySelectedDepts" #id
    __user_select_department__ = "listFilterAddButton_mySelectedDepts" #id
    __user_existing_extension_input_field__ = "myExistingExtensions[0]" #id
    __user_extension_template_dropdown__ = "templateName" #id
    __user_done_button__ = "(//input[@name='okbutton'])[1]" #xpath
    __user_add_new_extension_button__ = "addItem_extension" #id
    __user_delete__ = "changeThis0_img"  #id
    __user_edit__ = "changeThis0_img"
    __user_view_image__ = "viewThis0_img"  #id
    __user_select_checkbox__ = "selectItem"  #name
    __user_on_select_remove_button__ = "onRemoveSelected"  #name
    __user_print_button__ = "onPrintSelected"  #name
    __user_add_expected_msg__ = "Add operation successful for:"  #class
    __user_delete_expected_msg__ = "Remove operation successful for:"
    __user_delete_actual_msg__ = "responseMessage"  #class
    __user_add_actual_msg__ = "responseMessage"  #class

    def get_user_link(self):
        return self.get_element(self.__user__, "id")

    def get_user_addbutton(self):
        return self.get_element(self.__user_add_button__, "name")

    def set_user_name_input_range(self, input):
        self.sendKeys(input, self.__user_name_input_range__, "name")

    def get_users_viewbutton(self):
        return self.get_element(self.__user_view_button__, "name")

    def get_user_next_button(self):
        return self.get_element(self.__user_next_button__, "id")

    def get_user_apply_button(self):
        return self.get_element(self.__user_apply_button__, "id")

    def get_user_cancel_button(self):
        return self.get_element(self.__user_cancel_button__, "xpath")

    def get_user_password(self):
        return self.get_element(self.__user_password__, "name")

    def get_user_add_actual_msg(self):
        return self.get_element(self.__user_add_actual_msg__, "class")

    def set_user_first_name(self, value):
        self.sendKeys(value, self.__user_first_name__, "id")

    def set_user_last_name(self, value):
        self.sendKeys(value, self.__user_last_name__, "id")

    def set_user_id(self, value):
        self.sendKeys(value, self.__user_user_id__, "id")

    def set_user_password(self, value):
        self.sendKeys(value, self.__user_password__, "name")

    def set_user_confirm_password(self, value):
        self.sendKeys(value, self.__user_confirm_password__, "name")

    def set_user_email_id(self, value):
        self.sendKeys(value, self.__user_email_id__, "id")

    def set_user_alternate_first_name(self, value):
        self.sendKeys(value, self.__user_alternate_first_name__, "id")

    def set_user_alternate_last_name(self, value):
        self.sendKeys(value, self.__user_alternate_last_name__, "id")

    def set_user__business1(self, value):
        self.sendKeys(value, self.__user__business1__, "id")

    def set_user__business2(self, value):
        self.sendKeys(value, self.__user__business2__, "id")

    def set_user_mobile1(self, value):
        self.sendKeys(value, self.__user_mobile1__, "id")

    def set_user_mobile2(self, value):
        self.sendKeys(value, self.__user_mobile2__, "id")

    def get_user_department(self):
        return self.get_element(self.__user_department__, "id")

    def get_user_select_department(self):
        return self.get_element(self.__user_select_department__, "id")

    def set_user_existing_extension_input_field(self, extension):
        self.sendKeys(extension, self.__user_existing_extension_input_field__, "id")

    def get_user_extension_template_dropdown(self):
        return self.get_element(self.__user_extension_template_dropdown__, "id")

    def get_user_done_button(self):
        return self.get_element(self.__user_done_button__, "xpath")

    def get_user_add_new_extension_button(self):
        return self.get_element(self.__user_add_new_extension_button__, "id")

    def click_user_link(self):
        self.element_click(self.__user__,"id")

    def click_user_add_button(self):
        self.element_click(self.__user_add_button__,"name")

    def click_user_delete(self):
        self.element_click(self.__user_delete__,"id")

    def click_user_select_department(self):
        self.element_click(self.__user_select_department__, "id")

    def click_user_edit(self):
        self.element_click(self.__user_edit__,"id")

    def click_user_view_image(self):
        self.element_click(self.__user_view_image__,"id")

    def click_user_select_checkbox(self):
        self.element_click(self.__user_select_checkbox__,"name")

    def click_user_on_select_remove_button(self):
        self.element_click(self.__user_on_select_remove_button__, "name")

    def click_user_print_button(self):
        self.element_click(self.__user_print_button__, "name")

    def click_user_apply_button(self):
        self.element_click(self.__user_apply_button__, "id")

    def click_user_done_button(self):
        self.element_click(self.__user_done_button__, "xpath")

    def click_user_view_button(self):
        self.element_click(self.__user_view_button__,"name")








