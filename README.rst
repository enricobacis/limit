limit
=====

*python decorator that limits the calling rate of a function*

Description
-----------

.. image:: https://raw.githubusercontent.com/enricobacis/limit/master/.screenshot/limit.gif
    :target: https://asciinema.org/a/4f621lbwvpgf91neshex89nrm
    :align: center

This decorator limits the calling rate of the decorated function. This is
useful in conjuction with web API calls, where you often get banned if you
perform more calls than the ones specified in the terms of services.

The rate is ``limit`` over ``every``, where limit is the number of invocation
allowed every ``every`` seconds. ``limit(4, 60)`` creates a decorator that
limits the function calls to *4 per minute*. If not specified, ``every``
defaults to ``1`` second.

.. code:: python

    @limit(4, 60)
    def function(...):
        """never invoke this function more than 4 times per minute."""
        ...

Installation
------------

The package has been uploaded to `PyPI`_, so you can install it with pip:

    pip install limit


.. _PyPI: https://pypi.python.org/pypi/limit
