.. {{ cookiecutter.package_name }} documentation master file, created by {{ cookiecutter.author_name }}

{{ '=' * cookiecutter.project_name|length }}
{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

{{ cookiecutter.project_short_description }}

Links
*****

* Read the documentation on `Read the docs <https://{{ cookiecutter.package_name }}.readthedocs.io/>`_;
* Download its `PyPi package <https://pypi.python.org/pypi/{{ cookiecutter.package_name }}>`_;
* Clone it on its `Github repository <https://github.com/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}>`_;

Dependancies
************

* Python>=3.5;
* Click>=7.0,<8.0

User’s Guide
************

.. toctree::
   :maxdepth: 2

   install.rst

Developer’s Guide
*****************

.. toctree::
   :maxdepth: 1

   development.rst
   history.rst
