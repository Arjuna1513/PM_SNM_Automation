from base.selenium_driver import SeleniumDriver


class PM_OwnSettings_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Extensions = "Extensions"  #id
    __General = "General"  #id

    def click_Extensions(self):
        self.element_click(self.__Extensions, "id")

    def click_General(self):
        self.element_click(self.__General, "id")