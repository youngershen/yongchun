#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

import re
from regex import RE_FILE_NAME
from regex import RE_OUTPUT_TAG
from regex import RE_SPLITER_TAG
from regex import RE_OUTPUT_CONTENT_TAG

from exception import TemplateNotFoundError

RE_FILE_NAME_PATTERN   =  re.compile(RE_FILE_NAME)
RE_OUTPUT_TAG_PATTERN  = re.compile(RE_OUTPUT_TAG)
RE_SPLITER_TAG_PATTERN = re.compile(RE_OUTPUT_TAG)
RE_OUTPUT_CONTENT_TAG_PATTERN = re.compile(RE_OUTPUT_CONTENT_TAG)

class Render(object):
    def __init__(self, buffer, data):
        
        self.buffer = buffer
        self.data    = data
        self.buffer_node = [] 
    def rend_to_html(self):
        self.__find_tag_position()
        return self.rend_string()   

    def rend_string(self):
        if len(self.buffer_node) > 0 :
            for i,v in enumerate(self.buffer_node):
                ret = self.__parse_output_tag(v)
                if ret is not None:
                    self.buffer_node[i] = ret
        return ''.join(self.buffer_node)

    def __parse_tags(self):
        pass

    def __parse_output_tag(self, tag_str):
        m = re.match(RE_OUTPUT_TAG_PATTERN, tag_str)
        if m is not None:
           output_tag = m.group()
           im = re.search(RE_OUTPUT_CONTENT_TAG_PATTERN, output_tag)
           if im is not None:
               name = im.group()
               return self.data.get(name, None)
        return None

    def __find_tag_position(self):
        tag_buffer =re.findall(RE_SPLITER_TAG, self.buffer)
        node = re.split(RE_SPLITER_TAG, self.buffer)
        if len(tag_buffer) > 0 and len(node) > 0:
            for i,v in enumerate(node):
                self.buffer_node.append(v)
                if i < len(node) - 1:
                    self.buffer_node.append(tag_buffer[i])
    
        return self.buffer_node 

class Loader(object):
    dir_list = None
    
    def __init__(self, *args, **kwargs):
        if 'dir_list' in kwargs:
            self.dir_list = kwargs.get('dir_list', [])

    def load(self, target_name = None):
        if len(self.dir_list) < 1:
            return None
        elif target_name is None:
            return None
        else:
            for i, e in enumerate(self.dir_list):
                try:
                    path = e + target_name 
                    with open(path) as f:
                        buffer = f.read()
                except TemplateNotFoundError as e:
                    print e
                else:
                    return buffer

            return None

class Template(object):

    def __init__(self, *args, **kwargs):
        if 'template_dirs' in kwargs:
            self.template_dirs = kwargs.get('template_dirs', None)
        
        if 'template_name' in kwargs:
            self.template_name = kwargs.get('template_name', None)

        if 'template_encode' in kwargs:
            self.template_path = kwargs.get('template_encode', 'utf8')
        if 'data' in kwargs:
            data = kwargs.get('data', None)
            if data is not None and isinstance(data, dict):
                self.data = data
            else:
                self.data = None

    def rend_to_html(self):
        render = Render(self.template_buffer, self.data)
        ret = render.rend_to_html()
        with open('./index_rend.html', 'w') as f:
            f.write(ret)

    def load(self):
        self.__load_template()
        return self.template_buffer

    def __load_template(self):
        if self.template_dirs is not None and self.template_name is not None:
            loader = Loader(dir_list = self.template_dirs)
            self.template_buffer = loader.load(target_name = self.template_name)

