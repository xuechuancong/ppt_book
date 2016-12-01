# -*- coding:utf-8 -*-
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("calling {0}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@logger
def get_args(*args, **kwargs):
    print("*args={0}, **kwargs={1}".format(*args,**kwargs))

if __name__ == '__main__':
    get_args('hello','world')

