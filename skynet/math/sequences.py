def Fibonacci() :
    '''A Generator for the Fibonacci numbers.'''
    p, q = 0, 1

    while True :
        yield p
        p, q = q, p + q

def fibonacci(n) :
    '''Computes the nth Fibonacci number.'''

    if n in (0, 1) :
        return n

    if n % 2 :
        return fibonacci((n - 1) // 2) ** 2 + fibonacci((n + 1) // 2) ** 2
    else :
        return (2 * fibonacci((n // 2) - 1) + fibonacci(n // 2)) * fibonacci(n // 2)
