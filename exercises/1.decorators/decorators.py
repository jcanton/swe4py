# import functools

def momoize(function):
    cache = {}
    def wrapper(*args):
        print("I'm a wrapper")
        if args in cache:
            print("In cache")
            return cache[args]
        else:
            print("Not in cache")
            result = function(*args)
            cache[args] = result
            return result
    return wrapper

@momoize
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@momoize
def mul(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

add(2, 3)
mul(2, 3)