#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com
class Library(object):
    library = {}
    instance = None

    def __new__(klass, *args, **kwargs):
        if not klass.instance:
            return object.__new__(klass, *args, **kwargs)
        else:
            return klass.instance

    def __init__(self):
        self.temp_register_name = None
        super(Library, self).__init__()

    def get_library(self):
        print self.library

    def tag(self, tag_register_name = None):
        if tag_register_name is not None:
            self.temp_register_name = tag_register_name
        return self.wrapper 

    
    def wrapper(self, func):
        if not self.temp_register_name:
            self.temp_register_name = getattr(func, '__name__')
        self.library.update({self.temp_register_name : func})
        return func

def main():
    lib = Library()
    @lib.tag('repeat')
    def tag_repeat_func(params = None, context = None):
        print "test repeat"

    lib.get_library()

if __name__ == '__main__':
    main()

