.. _Cookiecutter: https://github.com/audreyr/cookiecutter

===========================
cookiecutter-sveetch-python
===========================

Yet another `Cookiecutter`_ template to produce a repository to start
a Python3 package.

It emphases on simple package with quality and not any relation to
any service (state badge, pyup, travis, etc..) except ReadTheDoc
link in README.

Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-python.git

Package content
    A Python3 package with everything to start:

    * Promote Test Driven Development;
    * Configuration in ``setup.cfg`` ready to upload package to Pypi;
    * Sample object to say hello world;
    * Sample commandline actions with Click;
    * Flake8 configuration for quality review;
    * Tests on sample object;
    * Tox configuration for tests;
    * Code is fully documented with ReStructuredText with Napoleon
      extension format.

    Package cover some basic features:

    * Object inheritance;
    * Click basic features;
    * Python logging usage;
    * Testing core, command line and logging;

Package requirements
    To use it from repository url you just need `Cookiecutter`_.

    However if you want to install it locally (to avoid doing request each time
    you use it) you will need virtualenv and use the ``make install`` from
    template Makefile. Once installed you can create a bash alias like: ::

        alias cookpy='/home/your/install/cookiecutter-sveetch-python/.venv/bin/cookiecutter /home/your/install/cookiecutter-sveetch-python'

    Once create the package itself have default requirements for
    ``click>=7.0,<8.0``, ``colorlog`` and ``colorama``. To install it from
    shipped Makefile you will also need ``virtualenv``.

Naming
    For a given ``Sample bar`` project name:

    * Package name will be ``sample-bar``;
    * Application name will ``sample_bar``;

    You can change package and application names during project creation.

Options
    You can define author full name, email, github username, pypi username,
    version start, package name and package short description.

    Some of these have a default value filled from a previous value, obviously
    you can edit it to your own needs.

    You can pre define some options in your
    `cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/1.7.2/advanced/user_config.html>`_
    to avoid to input it each time. This is especially recommended for the
    author and username ones.
