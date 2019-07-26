import xlrd
from utilities.Custom_Logger import CustomLogger
import logging
import pytest


class UserData():
    cl = CustomLogger().custom_logger(logging.INFO)
    def __init__(self, filename, sheet_name):
        self.file = "C:\\Users\\mallikar\\Documents\\Python_Workspace\\PM_SNM_Automation\\test_data\\"+filename+".xlsx"
        self.wBook = xlrd.open_workbook(self.file)
        self.sheet = self.wBook.sheet_by_name(sheet_name)
        self.totalRows = self.sheet.nrows
        self.totalCols = self.sheet.ncols

    def get_test_data(self, rowNumber, colNumber):
        return self.sheet.cell_value(rowNumber, colNumber)

    def parse_test_data(self,methodName, colNumber):
        value = None
        for row in range(self.totalRows):
            value = self.sheet.cell_value(row, 0)
            value = value.strip()
            if value == methodName.strip():
                userData = self.get_test_data(row, colNumber)
                userDataList = userData.split(",")
                return userDataList

    def get_IP_data(self, rowNumber, colNumber):
        IP = self.sheet.cell_value(rowNumber,colNumber)
        return IP

    def check_test_status(self,methodName):
        value = None
        for row in range(self.totalRows):
                value = self.sheet.cell_value(row,0)
                value = value.strip()
                if value == methodName:
                    flag = self.sheet.cell_value(row, 2)
                    if flag == 'N':
                        pytest.skip(self.cl.info("Skipped because Flag is set to N"))




