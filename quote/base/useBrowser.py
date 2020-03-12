# -*- coding: utf-8 -*-
# @Time    : 2020-03-11 10:35
# @Author  : baiping
# @qq      :376706275

from selenium import webdriver


class UseBrowser():

    driver=None

    def __init__(self):
        path = '../chromedriver.exe'
        # 实例化driver
        self.driver = webdriver.Chrome(path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        UseBrowser.driver=self.driver

    @classmethod
    def quit(cls):
        UseBrowser.driver.quit()

# if __name__=='__main__':
#     use = UseBrowser()
#     time.sleep(3)
#     UseBrowser.quit()
