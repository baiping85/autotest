# -*- coding: utf-8 -*-
# @Time    : 2020-03-11 10:47
# @Author  : baiping
# @qq      :376706275
from quote.base.operationbrowser import OperationBrowser
from quote.base.useBrowser import UseBrowser
from quote.util.exceloperation import ExcelOperation
from quote.util.yamloperation import YamlOperation


class LoginPage():

    def __init__(self):
        self.ob = OperationBrowser(UseBrowser.driver)
        self.eo=ExcelOperation('../config/logincase.xlsx')
        self.yo=YamlOperation('../config/locator.yaml')

    #封装login 功能
    def login(self,username='',password=''):
        self.ob.open_url(self.eo.get_excel_cell(1,1))
        self.ob.input_text_xpath(self.yo.get_locator('LoginPage','username'),username)
        self.ob.input_text_xpath(self.yo.get_locator('LoginPage','password'),password)
        self.ob.click_xpath(self.yo.get_locator('LoginPage','submit'))

    def success_info(self):
        self.ob.change_frame(self.yo.get_locator('LoginPage','framemain'))
        return self.ob.get_xpath_text(self.yo.get_locator('LoginPage','success_locator'))

