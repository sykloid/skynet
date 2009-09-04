from functools import wraps

def memoize(function) :
    cache = {}

    @wraps(function)
    def memoized_function(*args) :
        try :
            return cache[args]
        except KeyError :
            cache[args] = function(*args)
            return cache[args]

    return memoized_function
