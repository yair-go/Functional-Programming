# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:11:10 2018

@author: Yair
"""

def plus1(some_func):
    def inner(*args):
        print ("before ...")
        ret = some_func(*args)
        return ret + 1
    return inner

def foo(x):
    return 2 * x

@plus1
def bar(x):
    return 3 * x


if __name__ == "__main__" :
    dec = plus1(foo)
    print (dec(4))
    print (bar(2))

