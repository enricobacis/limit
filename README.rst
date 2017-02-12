limit
=====

*python decorator to limit the calling rate of functions*

Description
-----------

.. code:: python

    @limit(limit, every=1):
    def function(...):
        """never invoke this function more than 4 times per minute."""
        ...

This decorator limits the calling rate of the docorated function. The rate is
``limit`` over ``every``, where limit is the number of invocation allowed every
``every`` seconds. ``limit(4, 60)`` creates a decorator that limits the function
calls to *4 per minute*. If not specified, ``every`` defaults to ``1`` second.

This is useful in conjuction with API calls, where you often get banned if you
perform more calls than the ones specified in the terms of services.

Installation
------------

The package has been uploaded to `PyPI`_, so you can
install the package using pip:

    pip install limit


.. _PyPI: https://pypi.python.org