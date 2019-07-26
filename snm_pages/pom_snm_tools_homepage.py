from base.selenium_driver import SeleniumDriver

class SNM_Tools_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Command_Line = "Command_Line"  #id
    __Quality_of_Service = "Quality_of_Service"  #id
    __Signal_Tracing = "Tracing"  #id


    def click_Command_Line(self):
        self.element_click(self.__Command_Line, "id")

    def click_Quality_of_Service(self):
        self.element_click(self.__Quality_of_Service, "id")

    def click_Signal_Tracing(self):
        self.element_click(self.__Signal_Tracing, "id")