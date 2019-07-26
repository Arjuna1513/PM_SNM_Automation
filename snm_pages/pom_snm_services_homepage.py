from base.selenium_driver import SeleniumDriver

class SNM_Services_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Connections = "Connections"  #id
    __Messages = "Messages"  #id
    __Voice_Announcements = "Voice_Announcements"  #id
    __Media = "Medias"  #id
    __Branch_Office = "Branch_Office"  #id
    __RoutingServer = "RoutingServer"  #id
    __CSTAServer = "CSTAServer"  #id
    __Incoming_Call_Handling = "Incoming_Call_Handling"  #id
    __EnterpriseGateway = "EnterpriseGateway"  #id

    def click_Connections(self):
        self.element_click(self.__Connections, "id")

    def click_Mesages(self):
        self.element_click(self.__Messages, "id")

    def click_Voice_Announcements(self):
        self.element_click(self.__Voice_Announcements, "id")

    def click_Media(self):
        self.element_click(self.__Media, "id")

    def click_BranchOffice(self):
        self.element_click(self.__Branch_Office, "id")

    def click_RoutingServer(self):
        self.element_click(self.__RoutingServer, "id")

    def click_CSTA_Server(self):
        self.element_click(self.__CSTAServer, "id")

    def click_Incoming_Call_handling(self):
        self.element_click(self.__Incoming_Call_Handling, "id")

    def click_Enterprise_Gateway(self):
        self.element_click(self.__EnterpriseGateway, "id")