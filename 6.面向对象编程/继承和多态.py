#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Timer(object):
    def run(self):
        print('Start...')

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Timer())
