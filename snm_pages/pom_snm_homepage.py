from base.selenium_driver import SeleniumDriver


class SNM_HomePage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __initial_setup = "Initial_Setup"  #id
    __number_analysis = "Number_Analysis"  #id
    __telephony = "Telephony"  #id
    __services = "Services"  #id
    __system = "System"  #id
    __tools = "Tools"  #id
    __logs = "Logs"  #id
    __logout = " Logout"

    def get_initial_setup(self):
        return self.get_element(self.__initial_setup, "id")

    def get_number_analysis(self):
        return self.get_element(self.__number_analysis, "id")

    def get_telephony(self):
        return self.get_element(self.__telephony, "id")

    def get_services(self):
        return self.get_element(self.__services, "id")

    def get_system(self):
        return self.get_element(self.__system, "id")

    def get_tools(self):
        return self.get_element(self.__tools, "id")

    def get_logs(self):
        return self.get_element(self.__logs, "id")


    # Click elements
    def click_initial_setup(self):
        self.element_click(self.__initial_setup, "id")

    def click_number_analysis(self):
        self.element_click(self.__number_analysis, "id")

    def click_telephony(self):
        self.element_click(self.__telephony, "id")

    def click_services(self):
        self.element_click(self.__services, "id")

    def click_system(self):
        self.element_click(self.__system, "id")

    def click_tools(self):
        self.element_click(self.__tools, "id")

    def click_logs(self):
        self.element_click(self.__logs, "id")

    def click_logout(self):
        self.element_click(self.__logout, "link")