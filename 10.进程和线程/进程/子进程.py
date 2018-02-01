#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess


def normalSubprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


def Popen():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)


def dir():
    # shell=True 是为了让命令被操作系统命令处理器或shell解释
    lsout = subprocess.Popen(['dir', '*.*'], shell=True, stdout=subprocess.PIPE).stdout  # linux中dir换成ls
    for line in lsout:
        print(line.decode('gbk'))


def communite():
    ls = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
    lsout, lserr = ls.communicate()
    print(lsout.decode('utf8'))






if __name__ == '__main__':
    communite()
