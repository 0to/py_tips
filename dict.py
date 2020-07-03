#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Merging dictionaries
'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'd': 4}
# (Python 3.5+)
dict3 = {**dict1, **dict2}
dict4 = {**dict2, **dict1}
print('If there are overlapping keys, the keys from the first dictionary will be overwritten.')
print(dict3)  # This code will print: {'a': 3, 'b': 2, 'd': 4}
print(dict4)  # This code will print: {'a': 1, 'd': 4, 'b': 2}
