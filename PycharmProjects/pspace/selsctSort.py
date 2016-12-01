# -*- coding:utf-8 -*-

import sys
def selectSort(list):
    length = len(list)
    for i in range(length):
        minDex = i
        for j in range(i + 1, length):
            if (list[j] < list[minDex]):
                minDex = j

        if minDex != i:
            list[minDex], list[i] = list[i], list[minDex]

if __name__ == '__main__':
    A = [10, -3, 5, 7, 1, 3, 7]
    print 'Before sort:', A
    selectSort(A)
    print 'After sort:', A