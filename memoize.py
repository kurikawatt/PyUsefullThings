#coding: utf-8

def memoize(function):
    def memoized_function(*args):
        if args in memory:
            return memory[args]
        res = function(*args)
        memory[args] = res
        return res
    
    memory = {}
    return memoized_function

