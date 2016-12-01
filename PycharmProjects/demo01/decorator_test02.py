# -*- coding:utf-8 -*-

def second_decorator(func):
    pass

@second_decorator
def my_function():
    print("what will happend?")

if __name__ == '__main__':
    my_function()