#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

import re
from regex import RE_FILE_NAME
from regex import RE_OUTPUT_TAG
from regex import RE_SPLITER_TAG
from regex import RE_OUTPUT_CONTENT_TAG
from loader import CommonLoader
from exception import TemplateNotFoundError

RE_FILE_NAME_PATTERN   =  re.compile(RE_FILE_NAME)
RE_OUTPUT_TAG_PATTERN  = re.compile(RE_OUTPUT_TAG)
RE_SPLITER_TAG_PATTERN = re.compile(RE_OUTPUT_TAG)
RE_OUTPUT_CONTENT_TAG_PATTERN = re.compile(RE_OUTPUT_CONTENT_TAG)

class Template(object):

    def __init__(self, name, dirs = None, data = None):
        self.name = name
        if dirs is not None:
            self.dirs = dirs
        if data is not None:
            self.data = data
        self.html = None

    def rend_to_html(self):
        html = self.load()
        if self.data:


    def load(self):
        self.__load_template()
        return self.html

    def __load_template(self):
        if self.dirs is not None and self.name is not None:
            loader = CommonLoader(self.dirs, self.name)
            html = loader.load()
            if html is not None:
                self.html = html
