
=======
History
=======


Version 0.5.0 - 2025/07/13
--------------------------

This is a major release for a minor upgrade.

* [cookie] Upgraded to ``cookiecutter>=2.4.0``;
* [template] Removed support for Python<3.10;
* [template] Added support for Python 3.11;
* [template] Updated included script ``freezer.py`` to use ``importlib.metadata``
  instead of deprecated ``pkg_resources``;
* [template] Enabled Sphinx extension ``sphinx.ext.todo`` in documentation
  configuration;
* [template] Pinned various requirement to a minimal version to speed up Pip install;
* [template] Added dummy ``pyproject.toml`` to fix install with recent Pip and
  Setuptools. This is until template is fully moved to 'pyproject.toml';


Version 0.4.2 - 2023/10/15
--------------------------

* Changed RTD configuration, now it does not install from package anymore but directly
  from the package checkout so we are able to build RTD documentation from any
  temporary working branch;


Version 0.4.1 - 2023/08/23
--------------------------

* Fixed documentation requirements that did not used extra requirement ``[doc]`` that
  resulted on build failure on readthedocs;


Version 0.4.0 - 2023/08/21
--------------------------

This is a major upgrade to improve quality, documentation and package.


* [cookie] Started this history changelog;
* [cookie] Added ``_cookiecutter_sveetch_python_version`` variable to
  ``cookiecutter.json`` for versioning template;
* [cookie] Upgraded to ``cookiecutter>=2.3.0``;
* [cookie] Added Makefile task ``project`` to create projects in ``dist/``;
* [cookie] Added a new option ``init_git_repository`` to enabled for automatic GIT
  repository initialization on created project;
* [cookie] Added a new option ``include_cli`` to choose to keep the CLI or not;
* [cookie] Added a post hook to manage CLI files removing and GIT initialization
  depending options;
* [cookie] Removed requirement to ``jinja2-time``;
* [template] Fixed project test configuration;
* [template] Removed support for Python 3.6 and 3.7;
* [template] Updated ``.readthedocs.yml`` file to follow service deprecations changes;
* [template] Added ``cookiebaked.json`` to include used context in created project;
* [template] Defined ``project_urls`` option in package setup;
* [template] Removed deprecated encoding file start;
* [template] Fixed command line documentation;
* [template] Upgraded application ``__init__.py`` to the modern way to load version;
* [template] Upgraded documentation to a new theme, improved sphinx_reload script and
  moved it into ``docs/``;
* [template] Improved Makefile (better variable names and enabled ANSI color usage on
  task titles);
* [template] Included README in ``docs/index.rst`` instead of managing the same content
  twice;
* [template] Don't test all supported Python version in Tox config, only the min and
  max ones;
* [template] Splited extra requirements into various accurate extra spaces (dev,
  quality, release, etc..) to avoid making Tox installing useless stuff (like Flake8)
  for testing;
* [template] Improved ``flake`` task to include statistics and running everything (code
  and tests) in a single job;
* [template] Fixed ``exceptions.py`` to define class names named from package instead
  of dummy ``MyApp``;
