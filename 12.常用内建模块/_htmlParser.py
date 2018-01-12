#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('<%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

import re
from urllib import request


class MyHTMLParser(HTMLParser):
    _is_time = False
    _is_location = False
    _is_title = False

    def handle_starttag(self, tag, attrs):
        # attrs 返回一个list, list中的是一个个tuple 比如[('href', '/events/python-events/543/')]
        # attrs是start tag <>中的属性，以元组形式（name, value）返回（所有这些内容都是小写）
        if tag == 'time':
            self._is_time = True
        elif tag == 'span' and attrs and attrs[0][1] == 'event-location':
            self._is_location = True

        elif tag == 'a' and re.match(r'/events/python-events/[\d]+/', attrs[0][1]):
            self._is_title = True

    def handle_data(self, data):
        if self._is_time:
            print('Time: %s' % data)
            self._is_time = False
        elif self._is_title:
            print('Title: %s' % data)
            self._is_title = False
        elif self._is_location:
            print('Location: %s' % data)
            self._is_location = False
            print()


URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL, timeout=30) as f:
    data = f.read()

parse = MyHTMLParser()
parse.feed(str(data))
