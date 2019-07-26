from base.selenium_driver import SeleniumDriver

class SNM_NumberAnalysis_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Number_Plan = "Number_Plan"  #id
    __Call_Diversion = "Call_Diversion"  #id
    __Call_Discrimination = "Call_Discrimination"  #id
    __Emergency_Number = "Emergency_Number"  #id
    __Least_Cost_Route = "Least_Cost_Route"  #id

    def click_number_plan(self):
        self.element_click(self.__Number_Plan, "id")

    def click_call_diversion(self):
        self.element_click(self.__Call_Diversion, "id")

    def click_call_discrimination(self):
        self.element_click(self.__Call_Discrimination, "id")

    def click_emergency_number(self):
        self.element_click(self.__Emergency_Number, "id")

    def click_least_cost_route(self):
        self.element_click(self.__Least_Cost_Route, "id")
