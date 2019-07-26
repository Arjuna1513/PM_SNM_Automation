from base.selenium_driver import SeleniumDriver


class SNM_Login_Page(SeleniumDriver):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    __snm_user_id = "userId"  #name
    __snm_password = "password"  #name
    __snm_login_button = "login"  #name

    def get_snm_user_id(self):
        return self.get_element(self.__snm_user_id, "name")

    def get_snm_password(self):
        return self.get_element(self.__snm_password, "name")

    def get_snm_login_button(self):
        return self.__snm_login_button, "name"

    def set_snm_user_id(self, value):
        self.sendKeys(value,self.__snm_user_id,"name")

    def set_snm_password(self, value):
        self.sendKeys(value, self.__snm_password, "name")

    def click_snm_login_button(self):
        self.element_click(self.__snm_login_button, "name")

    def snm_login(self, userId, userPwd):
        self.set_snm_user_id(userId)
        self.element_click(self.__snm_password,"name")
        self.set_snm_password(userPwd)
        self.click_snm_login_button()