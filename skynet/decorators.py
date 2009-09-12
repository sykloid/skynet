from functools import wraps

def memoize(function) :
    function.cache = {}

    @wraps(function)
    def memoized_function(*args) :
        try :
            return function.cache[args]
        except KeyError :
            function.cache[args] = function(*args)
            return function.cache[args]

    return memoized_function
