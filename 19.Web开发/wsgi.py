#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server


def handle_index():
    with open('index.html', mode='rb') as f:
        data = f.read()
        f.close()
    return [data,]


def handle_date():
    return ['<h1>Page data</h1>'.encode('utf-8'),]


def handle_age():
    return ['<h1>Page age</h1>'.encode('utf-8'),]


def handle_404():
    return ['<h1>404 NOT FOUND</h1>'.encode('utf-8'),]


URL_DICT = {
    '/': handle_index,
    '/index': handle_index,
    '/date': handle_date,
    '/age': handle_age,
}


def run_server(environ, res):
    res('200 OK', [('Content-Type', 'text/html')])
    current_url = environ['PATH_INFO']
    print(current_url)
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
        return func()
    else:
        return handle_404()


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print('start to listen port 8000')
    httpd.serve_forever()
