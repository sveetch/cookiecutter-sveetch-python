.. _intro_cli:

============
Command line
============

Usage
-----

You may reach the tool either directly: ::

        .venv/bin/{{ cookiecutter.app_name }}

Or more simplier after environment have been activated: ::

    source .venv/bin/activate
    {{ cookiecutter.app_name }}

Help
----

There is the base tool help: ::

    {{ cookiecutter.app_name }} -h

And then each tool command has its own help: ::

    {{ cookiecutter.app_name }} greet -h
