.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Python: https://www.python.org
.. _virtualenv: https://virtualenv.pypa.io
.. _pip: https://pip.pypa.io
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.org
.. _Flake8: http://flake8.readthedocs.org
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _livereload: https://livereload.readthedocs.io
.. _Click: https://click.palletsprojects.com
.. _Read the Docs: https://readthedocs.org/
.. _Furo: https://github.com/pradyunsg/furo
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
.. _twine: https://twine.readthedocs.io

===========================
cookiecutter-sveetch-python
===========================

Yet another `Cookiecutter`_ template to produce a repository to start
a Python3 package.

It emphases on simple package with quality and not any relation to
any service (state badge, pyup, travis, etc..) except `Read the Docs`_
link in README.

A sample built from this template is available on repository
`sveetch-python-sample <https://github.com/sveetch/sveetch-python-sample>`_.


Features
********

Once created a project will have everything to start:

* Development in a Python virtual environment with `virtualenv`_ and `pip`_;
* Promote Test Driven Development with `Pytest`_;
* Configuration in ``setup.cfg`` ready to upload package to Pypi;
* Sample object to say hello world;
* Optional CLI sample with `Click`_;
* Optional GIT repository initialization;
* `Flake8`_ configuration for quality review;
* Tests on sample object;
* `tox`_ configuration for tests;
* Code is fully documented with `reStructuredText`_ and `Napoleon`_ extension for
  `Sphinx`_ with modern theme `Furo`_.
* Release with `twine`_.

Package cover some basic features:

* Object inheritance;
* Basic CLI features;
* Python logging usage;
* Testing core, command line and logging;


Usage
*****

Without installation
--------------------

Basically to use this cookie to create a new project you just need to install
`Cookiecutter`_ version 2.3.0 or latter: ::

    pip install cookiecutter>=2.3.0

You may then use it from its repository URL: ::

    cookiecutter https://github.com/sveetch/cookiecutter-sveetch-python.git


With local installation
------------------------

To speed up project creation you may install this cookie on your system.

First ensure you have `pip`_ and `virtualenv`_ packages installed and *GNU make*
available on your system. Then type: ::

    git clone https://github.com/sveetch/cookiecutter-sveetch-python.git
    cd cookiecutter-sveetch-python
    make install

.. Warning::

    You will need to update your install yourself opposed to the direct
    repository usage (*without install*) which always try to use the latest version
    from master branch.

    We recommend to reset it and reinstall it again: ::

        git pull origin master
        make clean install

Makefile task
.............

You can use the included Makefile task: ::

    make project

It will create all new project in ``dist/`` directory.


Bash alias
..........

Once installed you can also create shortcut with a bash alias in
your ``.bash_aliases``: ::

    alias cookpy='/home/foo/cookiecutter-sveetch-python/.venv/bin/cookiecutter /home/foo/cookiecutter-sveetch-python'

So you will just have to execute following command to create a new project: ::

    cookpy


Options
-------

You can define author full name, email, github username, pypi username,
version start, package name and package short description.

Some of these have a default value filled from a previous value, obviously
you can edit it to your own needs.

You can pre define some options in your
`cookiecutter user configuration <https://cookiecutter.readthedocs.io/en/latest/advanced/user_config.html>`_
to avoid some inputs. This is especially recommended for options related to author that
you should probably always use the same.


Naming
******

For a given ``Sample bar`` project name:

* Package name will be ``sample-bar``;
* Application name will ``sample_bar``;

You can change package and application names during project creation.
