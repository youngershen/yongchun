#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

import os
from exception import TemplateNotFoundError
from exception import DjangoSettingsNotFoundError

class BaseLoader(object):
   
    def __init__(self, dir_list= None, template_name= None):

        if dir_list:
            self.dir_list = dir_list
        if template_name:
            self.template_name = template_name

    def load(self, template_name = None):
        if template_name:
            self.template_name = template_name
        return self.load_template()

    def load_template(self):
        for i,e in enumerate(self.dir_list):
            template_path = ''.join((e,self.template_name))  
            template_path = os.path.abspath(template_path)
            if os.path.isfile(template_path):
                try:
                    with open(template_path) as file:
                        content = file.read()
                except IOError as e:
                    file.close()
                    print e
                else:
                    return content
        else:
            raise TemplateNotFoundError(self.template_name, template_path)

class CommonLoader(BaseLoader):
    pass

