#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

class TemplateError(Exception):
    """
        base template error exception
    """
    message = None
    template_name = None
    template_path = None

    def __init__(self, message = None):

        self.message = message
        Exception.__init__(self, message)

    @property
    def message(self):
        return self.message.decode('utf-8', 'replace')

    def __unicode__(self):
        return self.message or u''

class TemplateNotFoundError(IOError, LookupError, TemplateError):

    def __init__(self, template_name = None, template_path = None, message= None):
        self.message = message
        self.template_name = template_name
        self.template_path = template_path

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):

        return u"can not find template {template_path}, {message}".format(template_path = self.template_path, message = self.message)


class TemplateSyntaxError(TemplateError):
    def __init__(self, message= None, lineno = 0, name= None, file_path= None):
        TemplateError.__init__(self, message)
        self.lineno = lineno
        self.name = name
        self.file_path = file_path

    def __unicode__(self):
        return 'message : {message} \n lineno:{lineno} \n name:{name} \n file name : {\
                file_name}'.format(
                        message = self.message,
                        lineno = self.lineno,
                        name = self.name,
                        file_name = self.file_name
                        )

class DjangoSettingsNotFoundError(Exception):
    def __init__(self, app_name = None):
        if app_name:
            self.app_name = app_name

    def __unicode__(self):
        return u"can not import django setting maybe you are a fool"
