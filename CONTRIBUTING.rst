.. highlight:: console

============
Contributing
============

Contributions are welcome and greatly appreciated!
Contributions will always be credited.

How can I contribute?
---------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/romnn/classprop/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the `GitHub issues`_ for bugs. Anything tagged with *"bug"* and *"help
wanted"* is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub issues`_ for features. Anything tagged with *"enhancement"*
and *"help wanted"* is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

classprop could always use more documentation, whether as part of the
official classprop docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to `file an issue <https://github.com/romnn/classprop/issues>`_ on GitHub.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven open source project, so contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up classprop for local development.

1. Fork the `classprop repo <https://github.com/romnn/classprop>`_ on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/classprop.git

3. Install development dependencies into a virtual development environment (assuming you have ``pipenv`` installed)::

    $ cd classprop/
    $ pipenv install --dev
    $ invoke install-hooks

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you are ready to make changes. Remember to add tests to ``tests/`` and make sure all existing tests pass::

    $ pytest                                    # Run all tests
    $ pytest tests/one_specific_test_file.py    # Run one specific test
    $ tox                                       # Run the tests for different python versions

5. When you're done making changes, run all pre commit steps to make sure your changes pass all checks::

    $ invoke pre-commit

6. If you are done, commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website so your changes can
   be merged into the master.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the documentation (``docs/``)  should be updated. Put
   your new functionality into a function with a docstring and add the
   feature to the list in ``README.rst``.
3. The pull request should work for python 3.5+. Check the
   `build status of your pull request <https://travis-ci.com/romnn/classprop/pull_requests>`_
   and make sure that all tests pass for all supported python versions.

Publishing (Maintainers only)
-----------------------------

After merging the changes, tag your commits with a new version and push to GitHub::

$ bump2version (major | minor | patch)
$ git push --tags

.. _GitHub issues: https://github.com/romnn/classprop/issues
