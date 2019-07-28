from base.selenium_driver import SeleniumDriver

class PM_FunctionKeys(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    __continue_button = "onApplyButtonTopID"  #id
    __cancel_button = "(//input[@name='onCancelButton'])[1]"  #xpath
    __back_button = "multiStepBackButton"  #name
    __terminal_image_link = "//img[@src='./images/terminals/Aastra6869i.png']"  #xpath
    __functionKey2 = "funcKeyT2"  #id
    __functionKey3 = "funcKeyT3"  #id
    __functionKey4 = "funcKeyT4"  # id
    __functionKey5 = "funcKeyT5"  # id
    __functionKey6 = "funcKeyT6"  # id
    __functionKey7 = "funcKeyT7"  # id
    __functionKey8 = "funcKeyT8"  # id
    __functionKey9 = "funcKeyT9"  # id
    __functionKey10 = "funcKeyT10"  # id
    __functionKey11 = "funcKeyT11"  # id
    __functionKey12 = "funcKeyT12"  # id
    __functionKey13 = "funcKeyT13"  # id
    __functionKey14 = "funcKeyT14"  # id
    __functionKey15 = "funcKeyT15"  # id
    __functionKey16 = "funcKeyT16"  # id
    __functionKey17 = "funcKeyT17"  # id
    __functionKey18 = "funcKeyT18"  # id
    __functionKey19 = "funcKeyT19"  # id
    __functionKey20 = "funcKeyT20"  # id
    __functionKey21 = "funcKeyT21"  # id
    __functionKey22 = "funcKeyT22"  # id
    __functionKey23 = "funcKeyT23"  # id
    __functionKey24 = "funcKeyT24"  # id
    __functionKey25 = "funcKeyT25"  # id
    __functionKey26 = "funcKeyT26"  # id
    __functionKey27 = "funcKeyT27"  # id
    __functionKey28 = "funcKeyT28"  # id
    __functionKey29 = "funcKeyT29"  # id
    __functionKey30 = "funcKeyT30"  # id
    __functionKey31 = "funcKeyT31"  # id
    __functionKey32 = "funcKeyT32"  # id
    __functionKey33 = "funcKeyT33"  # id
    __functionKey34 = "funcKeyT34"  # id
    __functionKey35 = "funcKeyT35"  # id
    __functionKey36 = "funcKeyT36"  # id
    __functionKey37 = "funcKeyT37"  # id
    __functionKey38 = "funcKeyT38"  # id
    __functionKey39 = "funcKeyT39"  # id
    __functionKey40 = "funcKeyT40"  # id
    __functionKey41 = "funcKeyT41"  # id
    __functionKey42 = "funcKeyT42"  # id
    __functionKey43 = "funcKeyT43"  # id
    __functionKey44 = "funcKeyT44"  # id


    __functionKeyL1 = "funcKeyL1"  #id
    __key_lable = "keyLabel"  #id
    __function_key_dropdown = "keyFunction"  #id
    __dmn_input = "dmnDir"  #id
    __edn_input = "edn"  #id
    __gma_input = "groupNumber"  #id
    __mns_input = "mnsDir"  #id
    __pen_input = "penBossNumber"  #id
    __profile_list_dropdown = "keyOnCallList"  #id
    __rec_input = "uri"  #id
    __tns_input = "tnsDigit"  #id
    __sca_input = "scaDir"  #id
    __scabr_input = "scaDir"  #id
    __sxfer_input = "speedDialNo"  #id


    def click_continue_button(self):
        self.element_click(self.__continue_button, "id")

    def click_cancel_button(self):
        self.element_click(self.__cancel_button, "id")

    def click_back_button(self):
        self.element_click(self.__back_button, "id")

    def click_functionKey2(self):
        self.element_click(self.__functionKey2, "id")

    def click_functionKey3(self):
        self.element_click(self.__functionKey3, "id")

    def click_functionKey4(self):
        self.element_click(self.__functionKey4, "id")

    def click_functionKey5(self):
        self.element_click(self.__functionKey5, "id")

    def click_functionKey6(self):
        self.element_click(self.__functionKey6, "id")

    def click_functionKey7(self):
        self.element_click(self.__functionKey7, "id")

    def click_functionKey8(self):
        self.element_click(self.__functionKey8, "id")

    def click_functionKey9(self):
        self.element_click(self.__functionKey9, "id")

    def click_functionKey10(self):
        self.element_click(self.__functionKey10, "id")

    def click_functionKey11(self):
        self.element_click(self.__functionKey11, "id")

    def click_functionKey12(self):
        self.element_click(self.__functionKey12, "id")

    def click_functionKey13(self):
        self.element_click(self.__functionKey13, "id")

    def click_functionKey14(self):
        self.element_click(self.__functionKey14, "id")

    def click_functionKey15(self):
        self.element_click(self.__functionKey15, "id")

    def click_functionKey16(self):
        self.element_click(self.__functionKey16, "id")

    def click_functionKey17(self):
        self.element_click(self.__functionKey17, "id")

    def click_functionKey18(self):
        self.element_click(self.__functionKey18, "id")

    def click_functionKey19(self):
        self.element_click(self.__functionKey19, "id")

    def click_functionKey20(self):
        self.element_click(self.__functionKey20, "id")

    def click_functionKey21(self):
        self.element_click(self.__functionKey21, "id")

    def click_functionKey22(self):
        self.element_click(self.__functionKey22, "id")

    def click_functionKey23(self):
        self.element_click(self.__functionKey23, "id")

    def click_functionKey24(self):
        self.element_click(self.__functionKey24, "id")

    def click_functionKey25(self):
        self.element_click(self.__functionKey25, "id")

    def click_functionKey26(self):
        self.element_click(self.__functionKey26, "id")

    def click_functionKey27(self):
        self.element_click(self.__functionKey27, "id")

    def click_functionKey28(self):
        self.element_click(self.__functionKey28, "id")

    def click_functionKey29(self):
        self.element_click(self.__functionKey29, "id")

    def click_functionKey30(self):
        self.element_click(self.__functionKey30, "id")

    def click_functionKey31(self):
        self.element_click(self.__functionKey31, "id")

    def click_functionKey32(self):
        self.element_click(self.__functionKey32, "id")

    def click_functionKey33(self):
        self.element_click(self.__functionKey33, "id")

    def click_functionKey34(self):
        self.element_click(self.__functionKey34, "id")

    def click_functionKey35(self):
        self.element_click(self.__functionKey35, "id")

    def click_functionKey36(self):
        self.element_click(self.__functionKey36, "id")

    def click_functionKey37(self):
        self.element_click(self.__functionKey37, "id")

    def click_functionKey38(self):
        self.element_click(self.__functionKey38, "id")

    def click_functionKey39(self):
        self.element_click(self.__functionKey39, "id")

    def click_functionKey40(self):
        self.element_click(self.__functionKey40, "id")

    def click_functionKey41(self):
        self.element_click(self.__functionKey41, "id")

    def click_functionKey42(self):
        self.element_click(self.__functionKey42, "id")

    def click_functionKey43(self):
        self.element_click(self.__functionKey43, "id")

    def click_functionKey44(self):
        self.element_click(self.__functionKey44, "id")

    def click_Line1(self):
        self.element_click(self.__functionKeyL1, "id")

    def get_key_lable(self):
        return self.get_element(self.__key_lable, "id")

    def set_key_lable(self, value):
        self.sendKeys(value, self.__key_lable, "id")

    def get_function_key_dropdown(self):
        return self.get_element(self.__function_key_dropdown, "id")

    def get_dmn_input(self):
        return self.get_element(self.__dmn_input, "id")

    def set_dmn_input(self, value):
        self.sendKeys(value, self.__dmn_input, "id")

    def get_edn_input(self):
        return self.get_element(self.__dmn_input, "id")

    def set_edn_input(self, value):
        self.sendKeys(value, self.__edn_input, "id")

    def get_gma_input(self):
        return self.get_element(self.__gma_input, "id")

    def set_gma_input(self, value):
        self.sendKeys(value, self.__gma_input, "id")

    def get_mns_input(self):
        return self.get_element(self.__mns_input, "id")

    def set_mns_input(self, value):
        self.sendKeys(value, self.__mns_input, "id")

    def get_tns_input(self):
        return self.get_element(self.__tns_input, "id")

    def set_tns_input(self, value):
        self.sendKeys(value, self.__tns_input, "id")

    def get_sca_input(self):
        return self.get_element(self.__sca_input, "id")

    def set_sca_input(self, value):
        self.sendKeys(value, self.__sca_input, "id")

    def get_scabr_input(self):
        return self.get_element(self.__scabr_input, "id")

    def set_scabr_input(self, value):
        self.sendKeys(value, self.__scabr_input, "id")

    def get_sxfer_input(self):
        return self.get_element(self.__sxfer_input, "id")

    def set_sxfer_input(self, value):
        self.sendKeys(value, self.__sxfer_input, "id")

    def get_rec_input(self):
        return self.get_element(self.__rec_input, "id")

    def set_rec_input(self, value):
        self.sendKeys(value, self.__rec_input, "id")

    def get_pen_input(self):
        return self.get_element(self.__pen_input, "id")

    def set_pen_input(self, value):
        self.sendKeys(value, self.__pen_input, "id")

    def get_profile_list_dropdown(self):
        return self.get_element(self.__profile_list_dropdown, "id")

    