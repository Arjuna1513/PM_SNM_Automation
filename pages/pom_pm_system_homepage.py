from base.selenium_driver import SeleniumDriver


class PM_System_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Location = "Location"  #id
    __Subsystem = "Subsystem"  #id
    __Data_Management = "Data_Management"  #id
    __Options = "Options"  #id
    __Mail_Server = "Mail_Server"  #id
    __Configuration_Wizard = "Compact_Wizard"  #id
    __Batch_Operation = "Batch_Operation"  #id
    __Password_Settings = "Password_Settings"  #id

    def click_Location(self):
        self.element_click(self.__Location, "id")

    def click_Subsystem(self):
        self.element_click(self.__Subsystem, "id")

    def click_Data_Management(self):
        self.element_click(self.__Data_Management, "id")

    def click_Options(self):
        self.element_click(self.__Options, "id")

    def click_Mail_Server(self):
        self.element_click(self.__Mail_Server, "id")

    def click_Configuration_Wizard(self):
        self.element_click(self.__Configuration_Wizard, "id")

    def click_Batch_Operation(self):
        self.element_click(self.__Batch_Operation, "id")

    def click_Password_Settings(self):
        self.element_click(self.__Password_Settings, "id")