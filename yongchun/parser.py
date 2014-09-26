#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com
import re
from regex  import RE_SPLITER_TAG
from render import TemplateTagRender
from base   import Library

class BaseParser(object):
    pass

class HtmlParser(object):

    def __init__(self, content):
        if content:
            self.content = content
        else:
            self.content = None
        self.nodes = []
        self.content_walker_node = []
    
    def walk_nodes(self):
        return self.__build_all_tags_nodes()

    def __find_all_tag_nodes(self):
        nodes = re.findall(RE_SPLITER_TAG, self.content)
        return nodes

    def __build_all_tags_nodes(self):
        html_nodes = re.split(RE_SPLITER_TAG, self.content)
        all_html_nodes = []
        length = len(html_nodes)
        count = 0
        for i in range(0, length , 2):
            all_html_nodes.append(html_nodes[i])
            try:
                tag_content = html_nodes[i + 1]
            except IndexError as e:
                pass
            else:
                all_html_nodes.append(self.__make_tag(count, tag_content))
            count = count + 1

        return all_html_nodes

    def __make_tag(self, index, tag_content):
        tag_nodes = self.__find_all_tag_nodes()
        index = index + 1
        # 0 0|1  # 1 2|3  # 2 4|5
        inner_index = (index - 1) * 2 + 1 - 1
        ret_node = []
        ret_node.append(tag_nodes[inner_index])
        ret_node.append(tag_content)
        ret_node.append(tag_nodes[inner_index + 1])
        rendered_tag = TemplateTagRender(" ".join(ret_node)).parse_tag()

        #ret_tag_list = [ret_node, rendered_tag.htmlnode]
        #ret_tag_list = rendered_tag.parse_tag()
        #print ret_tag_list
        #return ret_tag_list
        return rendered_tag

def main():
    lib = Library()
    @lib.tag('repeat')
    def repeat(*args, **kwargs):
        return "test repeat tag"

    html = open('test.html').read()
    parser = HtmlParser(html)
    nodes = parser.walk_nodes()
    for i in nodes:
        print i
        print "==============================================================="

if __name__ == '__main__':
    main()
