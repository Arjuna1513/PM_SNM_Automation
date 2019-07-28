from base.selenium_driver import SeleniumDriver


class PM_Extension(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __extension_add_button = "onAddButton"  #name
    __template_dropdown = "templateName"  #name
    __manage_templates_link = "Manage Templates"  #link
    __mxone_version_dropdown_in_extension_homepage = "range"  #name
    __extensionType_dropdown_in_extension_homepage = "rangeFields[0]"  #name
    __enter_extension_value = "rangeFields[1]"  #name
    __enter_equipment_position = "rangeFields[2]"  #name
    __extension_view_button = "onViewRangeButton"  #name
    __rows_per_page_dropdown = "viewLimit"  #name
    __mxone_version_dropdown_in_extension_add_page = "nodeName"  #id
    __extensionType_dropdown_in_extension_addPage = "extensionType"  #id
    __multiple_extensions_checkbox = "multipleExtensions_CB"  #id
    __multipleExtensionsRange_dropdown = "multipleExtensionsRange"  #id
    __select_multiple_extension_number_series = "vacDir"  #id
    __multiple_extension_range_value = "extensionRange"  #id
    __extension_description_value = "myIPExtension_VO.extDescription"  ##name
    __server_dropdown = "myIPExtension_VO.GEDIP.LIM.LIMNumber"  #id
    __customer_dropdown = "myCustGroupName"  #id
    __CSP_dropdown = "myCSPName"  #id
    __Boss_Secretary_dropdown = "myIPExtension_VO.GEDIP.BSEC"  #id
    __backup_answering_position_number = "myIPExtension_VO.GEDIP.BCKPos"  # id
    __allow_security_exception_checkbox = "myIPExtension_VO.GEDIP.SECExc_CB"  #id
    __free_on_second_line_dropdown = "myIPExtension_VO.GEDIP.freeOnSecondLine"  #id
    __extension_first_name = "myIPExtension_VO.NIINP.name1"  #id
    __extension_second_name = "myIPExtension_VO.NIINP.name2"  #id
    __next_button = "onNextButtonTopID"  #id
    __apply_button = "onApplyButtonTopID"  #id
    __edit_authcode_button = "editItem_authorizationcode"  #id
    __edit_personalNumber_list = "editItem_personalnumber"  #id
    __phonetype_dropdown = "myIPExtPhoneType"  #id
    __panelType_dropdown = "myIPExtPanelType"  #id
    __function_keys_button = "changeItem_ipfunctionkeys"  #id
    __actual_add_response_message = "responseMessage"  #class
    __expected_add_response_message = "Add operation successful for:"
    __done_button = "okbutton"  #name




    ##__extension_add_button
    def click_extension_add_button(self):
        self.element_click(self.__extension_add_button, "name")

    ##__template_dropdown
    def get_template_dropdown(self):
        return self.get_element(self.__template_dropdown, "name")

    ##__manage_templates_link
    def click_manage_templates_link(self):
        self.element_click(self.__manage_templates_link, "link")

    ##__mxone_version_dropdown_in_extension_homepage
    def get_mxone_version_dropdown_in_extension_homepage(self):
        self.get_element(self.__mxone_version_dropdown_in_extension_homepage, "name")

    ##__extensionType_dropdown_in_extension_homepage
    def get_extensionType_dropdown_in_extension_homepage(self):
        self.get_element(self.__extensionType_dropdown_in_extension_homepage, "name")

    ##__enter_extension_value
    def get_enter_extension_value(self):
        return self.get_element(self.__enter_extension_value, "name")

    def set_enter_extension_value(self, value):
        self.sendKeys(value, self.__enter_extension_value, "name")

    ##__enter_equipment_position
    def get_enter_equipment_position(self):
        return self.get_element(self.__enter_equipment_position, "name")

    def set_enter_equipment_position(self, value):
        self.sendKeys(value, self.__enter_equipment_position, "name")

    ##__extension_view_button
    def click_extension_view_button(self):
        self.element_click(self.__extension_view_button, "name")

    ##__rows_per_page_dropdown
    def get_rows_per_page_dropdown(self):
        self.get_element(self.__rows_per_page_dropdown, "name")


    ## elements in page when add button is clicked
    ##__mxone_version_dropdown_in_extension_add_page
    def get_mxone_version_dropdown_in_extension_add_page(self):
        return self.get_element(self.__mxone_version_dropdown_in_extension_add_page, "id")

    ##__extensionType_dropdown_in_extension_addPage
    def get_extensionType_dropdown_in_extension_addPage(self):
        return self.get_element(self.__extensionType_dropdown_in_extension_addPage, "id")

    ##__multiple_extensions_checkbox
    def click_multiple_extension_checkbox(self):
        self.element_click(self.__multiple_extensions_checkbox, "id")

    ##__multipleExtensionsRange_dropdown
    def get_multipleExtensionsRange_dropdown(self):
        return self.get_element(self.__multipleExtensionsRange_dropdown, "id")

    ##__select_multiple_extension_number_series
    def get_multiple_extension_number_series(self):
        return self.get_element(self.__select_multiple_extension_number_series, "id")

    #__multiple_extension_range_value
    def set_multiple_extension_range_value(self, value):
        self.sendKeys(value, self.__multiple_extension_range_value, "id")

    #__extension_description_value
    def set_extension_description_value(self, value):
        self.sendKeys(value, self.__extension_description_value, "name")

    #Server dropdown
    def get_server_dropdown(self):
        return self.get_element(self.__server_dropdown, "id")

    #customer_dropdown
    def get_customer_dropdown(self):
        return self.get_element(self.__customer_dropdown, "id")

    #CSP dropdown
    def get_CSP_dropdown(self):
        return self.get_element(self.__CSP_dropdown, "id")

    #Boss secretary dropdown
    def get_Boss_Sceretary_dropdown(self):
        return self.get_element(self.__Boss_Secretary_dropdown, "id")

    #__backup_answering_position_number
    def set_backup_answering_position_number(self, value):
        self.sendKeys(value, self.__backup_answering_position_number, "id")

    #__allow_security_exception_checkbox
    def click_allow_security_exception_checkbox(self):
        self.element_click(self.__allow_security_exception_checkbox, "id")

    #__free_on_second_line_dropdown
    def get_free_on_second_line_dropdown(self):
        return self.get_element(self.__free_on_second_line_dropdown, "id")

    #__extension_first_name
    def get_extension_first_name(self):
        return self.get_element(self.__extension_first_name, "id")

    def set_extension_first_name(self, value):
        self.sendKeys(value, self.__extension_first_name,"id")

    #__extension_second_name
    def get_extension_second_name(self):
        return self.get_element(self.__extension_second_name, "id")

    def set_extension_second_name(self, value):
        self.sendKeys(value, self.__extension_second_name,"id")

    def click_next_button(self):
        self.element_click(self.__next_button, "id")

    def click_apply_button(self):
        self.element_click(self.__apply_button, "id")

    #__edit_authcode_button
    def click_edit_authcode_button(self):
        self.element_click(self.__edit_authcode_button, "id")

    #editItem_personalnumber
    def click_edit_personalNumberList_button(self):
        self.element_click(self.__edit_personalNumber_list, "id")

    #myIPExtPhoneType
    def get_phonetype_dropdown(self):
        return self.element_click(self.__phonetype_dropdown, "id")

    #myIPExtPanelType
    def get_panel_type_dropdown(self):
        return self.get_element(self.__panelType_dropdown, "id")

    #changeItem_ipfunctionkeys
    def click_function_keys_button(self):
        self.element_click(self.__function_keys_button, "id")

    #done_button
    def click_done_button(self):
        self.element_click(self.__done_button, "name")





