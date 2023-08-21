

.. include:: ../README.rst


Contents
********

.. toctree::
   :maxdepth: 2

   install.rst
   {% if cookiecutter.include_cli -%}cli.rst
   {% endif %}references/index.rst

About the project
*****************

.. toctree::
   :maxdepth: 1

   development.rst
   history.rst
