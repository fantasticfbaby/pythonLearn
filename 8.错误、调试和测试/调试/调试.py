#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
# import pdb
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    logging.info('n = %d' % n)
    # pdb.set_trace()
    print(10 / n)

def main():
    foo('0')


main()

