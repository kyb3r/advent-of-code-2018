import functools
import time

def timed(f):
    """
    Simple utility decorator which prints out 
    the execution time of the wrapped function.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = f(*args, **kwargs)
        end = time.monotonic()
        print(f'{f.__name__} - time taken: {(end-start) * 1000:.4f} ms')
        return result
    return wrapper

def memoized(callable):
    callable.cache = cache = {}
    @functools.wraps(callable)
    def wrapper(arg):
        if arg not in cache:
            cache[arg] = callable(arg)
        return cache[arg]
    return wrapper