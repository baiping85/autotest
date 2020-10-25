import HTMLTestRunner
import unittest
import sys

sys.path.append('C:\\.jenkins\\workspace\\Github')
from quote.util.exceloperation import ExcelOperation
from quote.base.operationbrowser import OperationBrowser
from quote.base.useBrowser import UseBrowser
from quote.page.login.loginpage import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        ub = UseBrowser()
        self.ob = OperationBrowser(UseBrowser.driver)
        self.eo=ExcelOperation('../config/logincase.xlsx')

    def test_login_1_success(self):
        loginpage = LoginPage()
        print(self.eo.get_excel_cell(1,2),self.eo.get_excel_cell(1,3))
        loginpage.login(self.eo.get_excel_cell(1,2),self.eo.get_excel_cell(1,3))
        info = loginpage.success_info()
        self.assertEqual(info,self.eo.get_excel_cell(1,4))

    def test_login_2_failed_null(self):
        loginpage = LoginPage()
        loginpage.login()
        error_info = self.ob.get_xpath_text('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[5]/td')

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    # 测试套件
    suite = unittest.TestSuite()
    # 加载用例
    login_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    # case放入列表
    lst_case = [login_case]
    # case加入套件
    suite.addTests(lst_case)
    # # runner运行
    # runner = unittest.TextTestRunner(verbosity=3)
    # 执行测试套件
    filename = '../report/index.html'
    fp = open(filename,'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1, title='login', description='logintest')
    runner.run(suite)
