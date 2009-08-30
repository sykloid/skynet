'''Tools to help time python code.'''

import timeit

class BasicTimer(object) :
    '''A basic timer for callables, using timeit.'''

    def __init__(self, function, setup = '', runs = 1000) :
        self.function = function
        self.setup = setup
        self.runs = runs

    def __call__(self, *args, **kwargs) :
        execution_string = "{}(*{}, **{})".format(
            self.function.__name__, args, kwargs
        )

        setup_string = "from __main__ import {};".format(
            self.function.__name__
        ) + self.setup

        self.timer = timeit.Timer(
            execution_string,
            setup_string,
        )

        print("{}: {} passes, {:.2f} μsec/pass".format(
            self.function.__name__,
            self.runs,
            1000000 * self.timer.timeit(number = self.runs) / self.runs
        ))
