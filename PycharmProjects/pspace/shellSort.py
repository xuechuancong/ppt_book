# -*- coding:utf-8 -*-

import sys


import sys
def shell_sort(a):
    ''''' shell排序
    '''
    a_len = len(a)
    gap = a_len/2
    while gap > 0:
        for i in range(a_len):
            m = i
            j = i + 1
            while j < a_len:
                if a[j] < a[m]:
                    m = j
                j += gap
            if m != i:
                a[m], a[i] = a[i], a[m]
        gap /= 2



if __name__ == '__main__':
    A = [8, -3, 5, 7, 1, 3, 7]
    print 'Before sort:', A
    shell_sort(A)
    print 'After sort:', A