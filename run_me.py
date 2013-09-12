#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
import random
import time
import sys
from power_console import printout

__author__ = 'nullexception'

if __name__ == '__main__':
    s = '72 97 112 112 121 32 80 114 111 103 114 97 109 109 101 114 115 32 68 97 121 33'
    print 'Message:'
    time.sleep(1)
    print s
    time.sleep(4)
    print 'Message decoding from ASCII. Please wait...'
    time.sleep(10)
    s = ''.join(map(chr, map(int, s.split())))
    for i in s:
        printout(i, random.randint(1, 7))
    print '\n'
    if sys.platform.startswith('win'):
        raw_input()

