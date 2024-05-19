#!/usr/bin/python3
"""
Module for calculating the fewest number of 
operations needed to result in exactly n H characters in the file.
"""
def minOperations(n):
    """ Minimum Operations"""
    if n <= 1:
        return 0
    i = 2
    res = 0
    while i <= n:
        if n % i == 0:
            res += i
            n = n / i
        else:
            i += 1
    return res
