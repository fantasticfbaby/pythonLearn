#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
import time

print('获取当前日期和时间')
now = datetime.now()
print(now)
print()
print('获取指定日期和时间')
dt = datetime(2018, 1, 10, 20, 41)
print(dt)
print()
print('datetime转换为timestamp')
dt = datetime(2018, 1, 10, 20, 41)
print(dt.timestamp())
print()
print('timestamp转换为datetime')
t = 1515588060.0
print(datetime.fromtimestamp(t))
print()
print('str转换为datetime')
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print()
print('datetime转换为str')
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print()
print('datetime加减')
now = datetime.now()
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))
print()
print('时区转换')
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo2_dt)
print()

'''
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
'''