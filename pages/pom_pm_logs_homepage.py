from base.selenium_driver import SeleniumDriver


class PM_Logs_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Audit_Trail = "Audit_Trail"  #id
    __Events = "Events"  #id
    __Security = "Security"  #id

    def click_Audit_Trail(self):
        self.element_click(self.__Audit_Trail, "id")

    def click_Events(self):
        self.element_click(self.__Events, "id")

    def click_Security(self):
        self.element_click(self.__Security, "id")