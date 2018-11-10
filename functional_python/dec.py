from functools import wraps

def outer():
    number = 5

    def inner():
        print(number)
    inner()

def apply(func, x, y): 
    return func(x,y)

def add(x, y): 
    return x + y

def sub(x, y): 
    return x - y

print(apply(add, 4,4))
print(apply(sub, 2,6))
def close(): 
    x= 5 
    def inner(): 
        print(x)
    return inner

def add_to_five(num): 
    def inner(): 
        print(num+5)
    return inner

fifteen = add_to_five(10)
fifteen()

def logme(func): 
    import logging 
    logging.basicConfig(level=logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs): 
        logging.debug("called {} with args {} and kwargs {}".format(
                func.__name__, args, kwargs))
        return func(*args, **kwargs)
    inner.__doc__ = func.__doc__
    inner.name = func.__name__
    return inner