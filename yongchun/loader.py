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

class DjangoLoader(BaseLoader):

    def __init__(self, app_name = None):
        if app_name:
            self.app_name = app_name
        self.init_django_settings()
        super(DjangoLoader, self).__init__() 

    def get_app_template_dirs(self):
        pass

class DjangoLoaderMixin(object):
    
    def init_django_settings(self):
        try:
            from django.conf import settings
        except ImportError as e:
            raise DjangoSettingsNotFoundError(app_name = self.app_name)
        else:
            self.django_settings = settings

    def get_app_template_dirs(self):
        pass
