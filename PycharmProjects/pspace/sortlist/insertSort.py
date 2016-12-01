#!/usr/bin/python
# -*- coding:utf-8 -*-

def insertSort(list):
    length = len(list)
    if length == 1:
        return list
    else:
        for i in range(1, length):
            for j in range(i, 0, -1):
                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]
    return list




if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print 'nums is:', nums
    insertSort(nums)
    print 'insert sort:', nums