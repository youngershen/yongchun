#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

import re
from regex import RE_SPLITER_TAG
from configuration import START_TOKEN
from configuration import END_TOKEN
from base import Library

class BaseNode(object):
    pass

class HtmlNode(BaseNode):
    def __init__(self):
        self.node_tag_name         = None
        self.node_tag_start_token  = None
        self.node_tag_end_token    = None
        self.node_tag_parameters   = None
        self.node_tag_content      = None

class TemplateTagRender(object):
    #  "<% repeat 3 %> sfsdf <% endrepeat %>"
    reg_tag_parameters = r"[a-zA-Z0-9\s]+"

    def __init__(self, match_string = None):
        if match_string:
            self.match_string = match_string
        else:
            self.match_string = None
        if self.match_string:
            self.library = Library()
            

    def parse_tag(self):
        contents = self.match_string.split() #re.split(RE_SPLITER_TAG, self.match_string)
        self.tag_name = contents[1]
        self.tag_start_token = contents[1]
        self.tag_end_token = contents[-2]
        self.content = contents[-4]
        parameters_pattern = re.compile(self.reg_tag_parameters)
        parameters_match   = re.search(parameters_pattern, ' '.join(contents[:-4]))
        if parameters_match:
            self.tag_parameters = parameters_match.group().strip()\
                    .partition(self.tag_start_token)[2].strip().split()
        else:
            self.tag_parameters = None

        htmlnode = HtmlNode()
        htmlnode.node_tag_name = self.tag_name
        htmlnode.node_tag_start_token  = self.tag_start_token
        htmlnode.node_tag_end_token = self.tag_end_token
        htmlnode.node_tag_parameters = self.tag_parameters
        htmlnode.node_tag_content = self.content
        self.htmlnode = htmlnode
        rendered_tag = self.rend_tag()
        return rendered_tag

    def rend_tag(self):
        if self.htmlnode and self.library:
            try:
                tag_func = self.library.library[self.htmlnode.node_tag_name]
                if tag_func is not None and callable(tag_func):
                    tag_ret = tag_func(self.htmlnode.node_tag_parameters)
                    return tag_ret
                else:
                    return ""
            except KeyError as e:
                return ""
                print e
        else:
            return ""
                    

    def get_html_node(self):
        return self.htmlnode
    def get_tag_parameters(self):
        return self.tag_parameters
    def get_tag_node(self):
        return self.content


    
    
