import functools as _functools
import threading as _threading


def limit(limit, every=1):
    """This decorator factory creates a decorator that can be applied to
       functions in order to limit the rate the function can be invoked.
       The rate is `limit` over `every`, where limit is the number of
       invocation allowed every `every` seconds.
       limit(4, 60) creates a decorator that limit the function calls
       to 4 per minute. If not specified, every defaults to 1 second."""

    def limitdecorator(fn):
        """This is the actual decorator that performs the rate-limiting."""
        semaphore = _threading.Semaphore(limit)

        @_functools.wraps(fn)
        def wrapper(*args, **kwargs):
            semaphore.acquire()

            try:
                return fn(*args, **kwargs)

            finally:                   # ensure semaphore release
                timer = _threading.Timer(every, semaphore.release)
                timer.setDaemon(True)  # allows the timer to be canceled on exit
                timer.start()

        return wrapper

    return limitdecorator
