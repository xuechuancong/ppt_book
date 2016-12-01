#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Xbonacci1(signature, n):
    l1 = len(signature)
    while len(signature) != n:
        s = sum(signature[-l1:])
        signature.append(s)
    return signature

def Xbonacci(signature, n):
    l1 = len(signature)
    for i in range(n-l1):
        s = sum(signature[-l1:])
        signature.append(s)
    return signature

if __name__ == '__main__':
    Xbonacci([1,1],10)
    for i in Xbonacci([1,1],10):
        print i

