# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 14:17
# @Author  : baiping
# @qq      :376706275
import yaml


class YamlOperation:

    def __init__(self,path):
        with open(path) as locator:
            self.data = yaml.load(locator,Loader=yaml.FullLoader)

    def get_locator(self,page,name):
        return self.data[page][name]