from base.selenium_driver import SeleniumDriver

class SNM_System_Homepage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __Backup_Restore = "Backup_Restore"  #id
    __Batch_Operation = "Batch_Operation"  #id
    __Hardware = "Hardware"  #id

    def click_Backup_Restore(self):
        self.element_click(self.__Backup_Restore, "id")

    def click_Batch_Operation(self):
        self.element_click(self.__Batch_Operation, "id")

    def click_Hardware(self):
        self.element_click(self.__Hardware, "id")