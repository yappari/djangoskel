=======================================
DjangoSkel -- a Django Project Skeleton
=======================================

This package provides a Django project skeleton. It creates a new Django
project, set and ready for deployment.
Basic usage::

    djangoskel <path/to/newproject> --project <project_name> --app <app_name>

Installation
============

DjangoSkel uses ``distribute`` for packaging. Just run::

    python setup.py install


Features
========

* Creates a Django 1.3.* project, with apps decoupled to a separate ``apps``
  directory.
* Adds `South <http://south.aeracode.org/>`_.
* Puts dependencies in a ``requirements.txt`` file for
  `pip <http://www.pip-installer.org/>`_.
* Creates WSGI and VHost templates.
* Provides a `Fabric <http://fabfile.org>`_ deployment script.
  It creates and uploads a tarball from the current git branch, so it
  only works if the project is managed with `git <http://git-scm.com/>`_.


Quick start
===========

After running::

    djangoskel <path/to/newproject> --project=<project_name> --app=<app_name>

there will be a new django project under ``<path/to/newproject>``
named ``<project_name>`` with one application called ``<app_name>``.
You can give deployment a test ride, by running from the project dir::

    git init; git add .; git commit -m 'initial commit'
    fab localhost setup

If everything goes well, a ``test-deployment`` directory should appear, with
a ``.vhost`` file ready for feeding to Apache.

For each new server you'll need to:

* add the server configuration to ``fabfile.py``
* ``fab <server_name> setup`` for first deployment
* fill out ``localsettings.py`` on the server (always re-deploy to apply)
* symlink the ``.vhost`` file to Apache's ``sites-enabled`` (or
  copy to ``sites-available``, edit and symlink, as the default file
  `will` be overwritten on the next deployment) and reload
* re-deploy with ``fab <server_name> deploy``


Dependencies
============

* `skeleton <https://github.com/yappari/skeleton>`_
* `git-archive-all.sh <https://github.com/yappari/git-archive-all.sh>`_
  (included)

Server-side dependencies
------------------------

* SSH access
* `virtualenv <http://virtualenv.org>`_ with bundled pip
* Apache with `mod_wsgi <http://code.google.com/p/modwsgi/>`_


Authors
=======

* Radek Czajka <radek.czajka@gmail.com>
