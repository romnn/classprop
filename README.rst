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

Your short description here. `romnnn.github.io/classprop <https://romnnn.github.io/classprop>`_

.. code-block:: console

    $ pip install classprop

See the `official documentation`_ for more information.

.. _official documentation: https://classprop.readthedocs.io

.. code-block:: python

    import classprop

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
