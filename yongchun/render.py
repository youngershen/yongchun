#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

import re
from regex import RE_SPLITER_TAG
from configuration import START_TOKEN
from configuration import END_TOKEN

class TemplateTag(object):
    tag_name         =  "tag_repeat"
    start_tag_token  =  "repeat"
    end_tag_token    =  "endrepeat"

    #  "<% repeat 3 %> sfsdf <% endrepeat %>"
    reg_tag_parameters = r"[a-zA-Z0-9\s]+"

    def __init__(self, match_string = None):
        if match_string:
            self.match_string = match_string
        else:
            self.match_string = None
        if self.match_string:
            self.parse_tag()
    
    def parse_tag(self):
        contents = self.match_string.split() #re.split(RE_SPLITER_TAG, self.match_string)
        self.content = contents[-4]
        parameters_pattern = re.compile(self.reg_tag_parameters)
        parameters_match   = re.search(parameters_pattern, ' '.join(contents[:-4]))
        if parameters_match:
            self.tag_parameters = parameters_match.group().strip()\
                    .partition(self.start_tag_token)[2].strip().split()
        else:
            self.tag_parameters = None

    def get_tag_parameters(self):
        return self.tag_parameters
    
    def get_tag_node(self):
        return self.content

class RepeatTag(TemplateTag):
    tag_name        = "tag_repeat"
    start_tag_token = "repeat"
    end_tag_token   = "endrepeat"


class Reander(object):
    pass
    
