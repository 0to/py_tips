#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
https://www.python.org/dev/peps/pep-0515/
Python-Version:	3.6
为了方便阅读，较大的数字可以使用下划线进行连接。
'''
assets0 = 100_000_000
assets1 = int('100_000_000')
print(assets0, assets1)


'''
Rounding seems easy, round(1.1) evaluates to 1, round(1.8) evaluates to 2.
The question is, how do we round the .5 numbers?
Should you round up? down? Turns out, there are a lot of ways to do it..
Python 3 uses bankers rounding. Odd numbers are rounded up, even numbers are rounded down.
https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
The reasoning behind this method is that if you round a list of numbers, assuming there’s roughly the same number of odd and even numbers, the error (rounding) will cancel each other.
'''
print(round(1.5), round(2.5))  # This code will print: 2 2
print(round(1.6), round(2.6))  # This code will print: 2 3
print(round(1.4), round(2.4))  # This code will print: 1 2
