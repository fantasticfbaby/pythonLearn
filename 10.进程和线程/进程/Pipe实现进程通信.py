#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process, Pipe
import time, random

# 写数据进程执行的代码：
def write(pipe):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        pipe.send(value)
        time.sleep(random.random())


# 读数据进程执行的代码：
def read(pipe):
    print('Process to read: %s' % os.getpid())
    while True:
        value = pipe.recv()
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    (writerEnd, readerEnd) = Pipe()
    writer = Process(target=write, args=(writerEnd,))
    reader = Process(target=read, args=(readerEnd,))

    writer.start()
    reader.start()
    writer.join()
    reader.terminate()
