from base.selenium_driver import SeleniumDriver

class SNM_Telephoney_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Extensions = "Extensions"  #id
    __Operator = "Attendant"  #id
    __CallCenter = "Telephony_Call_Center"  #id
    __Groups = "Groups"  #id
    __External_Line = "External_Line"  #id
    __SystemData = "SystemData"  #id
    __IP_Phone = "IP_Phone"  #id
    __DECT = "DECT"  #id

    def click_Extensions(self):
        self.element_click(self.__Extensions, "id")

    def click_Operator(self):
        self.element_click(self.__Operator, "id")

    def click_Callcenter(self):
        self.element_click(self.__CallCenter, "id")

    def click_Groups(self):
        self.element_click(self.__Groups, "id")

    def click_ExternalLines(self):
        self.element_click(self.__Extensions, "id")

    def click_SystemData(self):
        self.element_click(self.__SystemData, "id")

    def click_IP_Phone(self):
        self.element_click(self.__IP_Phone, "id")

    def click_Dect(self):
        self.element_click(self.__DECT, "id")
