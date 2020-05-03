# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 14 Assignment

#Part 1
def fibonacci(n=int):
    if n<0:
        print("Parameter must be 0 or greater")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)       

#Part 2

def gcd(a, b):
    while b:
        (a,b) = (b, (a % b))
    return a

#Part 3
def compareTo(s1,s2):
    if len(s1) == len(s2):
        return 0
    elif len(s1) < len(s2):
        return -1, "string length of s1 is less than string length of s2"
    elif len(s1) > len(s2):
        return 1, "string length of s1 is greater than string length of s2"
