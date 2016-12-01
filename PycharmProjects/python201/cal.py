#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cal(x, y):
    a = max(x, y)
    b = min(x, y)
    if a == b:
        print 'cal: %s' %a
        return a
    else:
        return cal(b, a-b)# 更相减损术求最大公约数

def lcm(x, y):
    a = max(x, y)
    b = min(x, y)
    lcm = a*b/cal(x,y)
    print 'lcm: %s' %lcm
    return lcm

def nlcm(array):
    le = len(array)
    if le == 1:
        return array[le-1]
    else:
        return lcm(array[le-1], nlcm(array[:(le-1)]))
        #递归，先计算前两个数的最小公倍数，将该最小公倍数与第三个数，接着求最小公倍数

def convertFracts(lst):
    l = len(lst)
    array = []
    for i in range(l):
        array.append(lst[i][1])
        #将第二项放进一个列表中
    lst_nlcm = nlcm(array)
    print lst_nlcm
    # 求得第二项的最大公倍数
    s = []
    for i in range(l):
        print lst_nlcm*lst[i][0]/lst[i][1], lst_nlcm
        s.append([lst_nlcm*lst[i][0]/lst[i][1], lst_nlcm])
    return s


if __name__ == '__main__':
    # cal(49, 63)
    # lcm(2,4)
    # nlcm([2,3,4,7])
    convertFracts([[1,2],[1,3],[1,4]])




