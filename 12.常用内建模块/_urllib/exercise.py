#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        return json.loads(f.read())

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(json.dumps(data, indent=2))
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')


