# -*- coding:utf-8 -*-

def first_decorator(func):
    return func

@first_decorator
def my_function():
    print("a simple test decorator")


if __name__ == '__main__':
    my_function()