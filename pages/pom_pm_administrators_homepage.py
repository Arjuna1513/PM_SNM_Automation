from base.selenium_driver import SeleniumDriver


class PM_Administrators_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Administrator = "Administrator"  #id

    def click_Administrator_tab(self):
        self.element_click(self.__Administrator, "id")