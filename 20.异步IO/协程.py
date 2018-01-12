#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def consumer():
    r = 'a'
    while True:
        print('print:%s' % ('haha'))
        n = yield r
        if not n:
            print('RETURN')
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    r = c.send(None)
    n = 0
    print(r)
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
        print()
    c.close()


c = consumer()
produce(c)
# 自我理解过程：
# produce 先sendNone，启动生成器，consumer运行5,6,7行，运行到第8行时返回r，暂停
# 之后 produce sendN，consumer接收n赋值给consumer中的n，一直运行到结尾后继续运行开头7,8行，返回r，暂停
# produce close 后结束
'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

首先调用c.send(None)启动生成器；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

consumer通过yield拿到消息，处理，又通过yield把结果传回；

produce拿到consumer处理的结果，继续生产下一条消息；

produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”
'''
