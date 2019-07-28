from base.selenium_driver import SeleniumDriver

class PM_Authcode(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __authcode_add_button = "onAddButton"  #name
    __authcode_continue_button = "multiStepBackButton"  #name
    __authcode_apply_button = "onApplyButtonTopID"  #id
    __authcode_cancel_button = "onCancelButton"  #name
    __authcode_input_field = "myAuthorizationCode_VO.AUCOPs.indAUCOP[0].AUTH"  #name
    __hashType_dropdown = "myHashType"  #id
    __call_logging_input_field = "myAuthorizationCode_VO.AUCOPs.indAUCOP[0].CILCode"  #name
    __customer_dropdwon = "myCustGroupName"  #id
    __my_csp_dropdown = "myCSPName"  #id
    __authode_extension_usage = "myAuthorizationCode_VO.AUCOPs.indAUCOP[0].restrict_CB"  #id
    __change_button = "onChangeSelected"  #name
    __remove_button = "onRemoveSelected"  #name
    __print_authcodes = "onPrintSelected"  #name
    __select_authcode_checkbox = "selectItem"  #name
    __view_0th_item = "viewThis0_img"  #id
    __edit_0th_item = "changeThis0_img" #id
    __delete_0th_item = "removeThis0_img"  #id


    def click_authcode_add_button(self):
        self.element_click(self.__authcode_add_button, "name")

    def click_authcode_continue_button(self):
        self.element_click(self.__authcode_continue_button, "name")

    def click_authcode_apply_button(self):
        self.element_click(self.__authcode_apply_button, "id")

    def click_authcode_cancel_button(self):
        self.element_click(self.__authcode_cancel_button, "name")

    def get_authcode_input_field(self):
        return self.get_element(self.__authcode_input_field, "name")

    def set_authcode_input_field(self, value):
        self.sendKeys(value, self.__authcode_input_field, "name")

    def get_hashType_dropdown(self):
        return self.get_element(self.__hashType_dropdown, "id")

    def get_call_logging_input_field(self):
        return self.get_element(self.__call_logging_input_field, "name")

    def set_call_logging_input_field(self, value):
        self.sendKeys(value, self.__call_logging_input_field, "name")

    def get_customer_dropdown(self):
        return self.get_element(self.__customer_dropdwon, "id")

    def get_my_csp_dropdown(self):
        return self.get_element(self.__my_csp_dropdown, "id")

    def click_authode_extension_usage_checkbox(self):
        self.element_click(self.click_authode_extension_usage_checkbox(), "id")

    def click_change_button(self):
        self.element_click(self.__change_button, "name")

    def click_remove_button(self):
        self.element_click(self.__remove_button, "name")

    def click_print_authcodes(self):
        self.element_click(self.__print_authcodes, "name")

    def click_authcode_check_box(self):
        self.element_click(self.__select_authcode_checkbox, "name")

    def click_view_0th_item(self):
        self.element_click(self.__view_0th_item, "id")

    def click_edit_0th_item(self):
        self.element_click(self.__edit_0th_item, "id")

    def click_delete_0th_item(self):
        self.element_click(self.__delete_0th_item, "id")
