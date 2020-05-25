#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
datetime约定了范围，如果超出的话会报ValueError；
'''
from datetime import datetime

print(datetime.min)  # This code will print:  0001-01-01 00:00:00
print(datetime.max)  # This code will print:  9999-12-31 23:59:59.999999
# This code will print:  ValueError: year 10000 is out of range
date = datetime(10_000, 1, 1)
