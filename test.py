#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com
import os

from yongchun.template import Template
from yongchun.loader import BaseLoader
from yongchun.exception import TemplateNotFoundError
from yongchun.render import RepeatTag

def main():
    dirs = [os.getcwd() + '/']
    data = {'name' : 'younger'}
    template = Template(template_dirs = dirs, template_name = 'index.html', data = data)
    template.load()
    template.rend_to_html()

def  test_baseloader():
    dir_list = ['./']
    template_name = 'index.html'
    loader = BaseLoader(dir_list = dir_list, template_name = template_name)
    template = loader.load()
    print template

def test_tag():
    match_string = "<% repeat 10 %> sdfsfdsdf <% endrepeat %>"
    tag = RepeatTag(match_string = match_string)
    print tag.get_tag_parameters()
    print tag.get_tag_node()

if __name__ == '__main__':
    test_tag()
