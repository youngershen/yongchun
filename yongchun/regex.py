#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com
from configuration import START_TOKEN
from configuration import END_TOKEN
from configuration import OUTPUT_START_TOKEN

RE_FILE_NAME = r'(\w)+\.(\w)+'
RE_OUTPUT_TAG = r'{OUTPUT_START_TOKEN}[0-9a-zA-Z\._\s]*{END_TOKEN}'.format(OUTPUT_START_TOKEN = OUTPUT_START_TOKEN, END_TOKEN = END_TOKEN)
RE_SPLITER_TAG = r'{START_TOKEN}.*{END_TOKEN}'.format(START_TOKEN = START_TOKEN, END_TOKEN = END_TOKEN)
RE_OUTPUT_CONTENT_TAG = r'[a-zA-Z\._]+'

