# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 11:36
# @Author  : baiping
# @qq      :376706275

import xlrd
#获取工作薄对象
# workbook=xlrd.open_workbook('D:\\AutoTestCase\\logincase.xlsx')
# sheet=workbook.sheet_by_index(1)
# print(sheet.cell_value(1,1))

class ExcelOperation():

    def __init__(self,path,sheet=None):
        if sheet == None:
            sheet=1
        #获取工作薄
        self.workbook = xlrd.open_workbook(path)
        #获取sheet页面
        self.sheet =self.workbook.sheet_by_index(sheet)
    #获取单元格
    def get_excel_cell(self,nrow,ncol):
        return self.sheet.cell_value(nrow,ncol)

# if __name__=='__main__':
#     eo = ExcelOperation('../config/logincase.xlsx')
#     print(eo.get_excel_cell(1,1))