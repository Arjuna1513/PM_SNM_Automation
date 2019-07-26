from base.selenium_driver import SeleniumDriver

class SNM_Tools_CommandLine(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __commandField_Input_Text_Box = "commandField"  #name
    __cmdApply_Button = "cmdApply"  #name
    __browse_Button = "inputFile"  #name
    __execute_Button = "apply"  #name
    __clear_Window_Button = "clearWindow"  #name
    __close_window_Button = "close_window"  #name
    __command_Frame = "CommandLine"  #name


    def get_command_field_text_box(self):
        return self.get_element(self.__commandField_Input_Text_Box, "name")

    def get_command_apply_button(self):
        return self.get_element(self.__cmdApply_Button, "name")

    def get_command_browse_button(self):
        return self.get_element(self.__browse_Button, "name")

    def get_execute_button(self):
        self.get_element(self.__execute_Button, "name")

    def get_clear_window_button(self):
        return self.get_element(self.__clear_Window_Button, "name")

    def get_close_window_button(self):
        return self.get_element(self.__close_window_Button, "name")

    def get_commandFrame(self):
        return self.get_element(self.__command_Frame, "name")


    def set_command_filed_text_box(self, value):
        self.sendKeys(value, self.__commandField_Input_Text_Box, "name")

    def click_command_apply_button(self):
        self.element_click(self.__cmdApply_Button, "name")

    def click_browse_button(self):
        self.element_click(self.__browse_Button, "name")

    def click_execute_button(self):
        self.element_click(self.__execute_Button, "name")

    def click_clear_window_button(self):
        self.element_click(self.__clear_Window_Button, "name")

    def click_close_window_button(self):
        self.element_click(self.__close_window_Button, "name")