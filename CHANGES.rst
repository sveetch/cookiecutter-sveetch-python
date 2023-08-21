
=======
History
=======

Version 0.4.0 - Unreleased
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
