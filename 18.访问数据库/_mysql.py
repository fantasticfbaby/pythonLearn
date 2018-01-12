#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()
try:
    # 创建user表:
    cursor.execute('create table if not exists user (id int primary key auto_increment, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (name) values (%s)', ['tengfei'])
    print(cursor.rowcount)
    # 提交事务:
    conn.commit()
except:
    conn.rollback()
cursor.close()
# 运行查询:
cursor = conn.cursor()
try:
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)
except:
    print('Error: unable to fecth data')
# 关闭Cursor和Connection:
cursor.close()
print(True)
conn.close()
