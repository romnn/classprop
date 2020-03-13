===============================
classprop
===============================

.. image:: https://travis-ci.com/romnnn/classprop.svg?branch=master
        :target: https://travis-ci.com/romnnn/classprop
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/classprop.svg
        :target: https://pypi.python.org/pypi/classprop
        :alt: PyPI version

.. image:: https://img.shields.io/github/license/romnnn/classprop
        :target: https://github.com/romnnn/classprop
        :alt: License

.. image:: https://readthedocs.org/projects/classprop/badge/?version=latest
        :target: https://classprop.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/romnnn/classprop/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/romnnn/classprop
        :alt: Test Coverage

""""""""

.. role:: python(code)
   :language: python

Small python package that provides a :python:`@classproperty` decorator for python classes
that works just like :python:`@property` except for class variables!

.. code-block:: console

    $ pip install classprop

Use it just like builtin :python:`@property`'s:

.. code-block:: python

    from classprop import classprop

    class TestClass:
        _internal = "Hello, World"

        @classprop
        def my_class_prop(self) -> str:
            return self._internal

        @my_class_prop.setter
        def my_class_prop(self, value: str) -> None:
            self._internal = value



    foo = TestClass()
    assert foo.my_class_prop == "Hello, World"

    baz = TestClass()
    assert baz.my_class_prop == "Hello, World"

    baz.my_class_prop = "Changed"
    assert foo.my_class_prop == "Changed"


Development
-----------

For detailed instructions see `CONTRIBUTING <CONTRIBUTING.rst>`_.

Tests
~~~~~~~
You can run tests with

.. code-block:: console

    $ invoke test
    $ invoke test --min-coverage=90     # Fail when code coverage is below 90%
    $ invoke type-check                 # Run mypy type checks

Linting and formatting
~~~~~~~~~~~~~~~~~~~~~~~~
Lint and format the code with

.. code-block:: console

    $ invoke format
    $ invoke lint

All of this happens when you run ``invoke pre-commit``.

Note
-----

This project is still in the alpha stage and should not be considered production ready.
