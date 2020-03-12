# -*- coding: utf-8 -*-
# @Time    : 2020-03-11 10:42
# @Author  : baiping
# @qq      :376706275
import time




class OperationBrowser():

    def __init__(self,driver):
        self.driver=driver

    def open_url(self,url):
        self.driver.get(url)

    def input_text_xpath(self,locator,text):
        self.driver.find_element_by_xpath(locator).send_keys(text)

    def click_xpath(self,locator):
        self.driver.find_element_by_xpath(locator).click()

    def change_frame(self,name):
        # 切到父窗体
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(name)

    def get_xpath_text(self,locator):
        return self.driver.find_element_by_xpath(locator).text


# if __name__== '__main__':
#     ub = UseBrowser()
#     ob = OperationBrowser(UseBrowser.driver)
#     ob.open_url('http://localhost:8080/JavaPrj_6/')
#     ob.input_text_xpath('//*[@id="UserName"]','admin')
#     ob.input_text_xpath('//*[@id="Password"]','admin')
#     ob.click_xpath('/html/body/table/tbody/tr[1]/td[2]/form/table/tbody/tr[6]/td/input[1]')
#     time.sleep(3)
#     UseBrowser.quit()
