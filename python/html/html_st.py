#!/usr/bin/env python3

import sys
import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

s1 = 'abc'


class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.href_list = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        print("Start tag:[{}]".format(self.getpos()), tag)
        for attr in attrs:
            print("     attr:", attr)
            if attr[0] == 'href':
                self.href_list.append(attr[1])

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)


url = 'https://docs.python.org/3/library/index.html'
request_time_out = 20
r = requests.get(url, timeout=request_time_out)

c1 = '''<html><head><title>Test</title></head>
            <body><h1>Parse me!</h1></body></html>'''
parser = MyHTMLParser()
parser.feed(r.content.decode())

# [print(x) for x in parser.href_list]
