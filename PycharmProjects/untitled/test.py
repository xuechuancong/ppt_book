#! /usr/bin/env

def is_odd(n):
    return n%2 == 1

for i in list(filter(is_odd, [2,3,4,5,6,76])):
    print(i)
# for i in [1,3,4]:
#     print(i)
