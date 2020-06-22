.. _Cookiecutter: https://github.com/audreyr/cookiecutter

===========================
cookiecutter-sveetch-python
===========================

Yet another `Cookiecutter`_ template to produce a repository to start
a Python3 package.

It emphases on simple package with quality and not any relation to
any service (state badge, pyup, travis, etc..) except preview ReadTheDoc
link in README.

Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-python.git

Package content
    A Python3 package with everything to start:

    * Configuration in ``setup.cfg`` ready to upload package to Pypi;
    * Sample object;
    * Flake8 configuration for quality review;
    * Tests on sample object;
    * Tox configuration for tests;

Package requirements
    Basic package requirements are virtualenv and ...

Naming
    For a given ``Sample bar`` project name:

    * Package name will be ``sample-bar``;
    * Application name will ``sample_bar``;

    You can change package and application names during project creation.
