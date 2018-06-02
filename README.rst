===========
Lines Table
===========


.. image:: https://img.shields.io/pypi/v/lines_table.svg
        :target: https://pypi.python.org/pypi/lines_table

.. image:: https://img.shields.io/travis/bobm123/lines_table.svg
        :target: https://travis-ci.org/bobm123/lines_table

.. image:: https://readthedocs.org/projects/lines-table/badge/?version=latest
        :target: https://lines-table.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/bobm123/lines_table/shield.svg
     :target: https://pyup.io/repos/github/bobm123/lines_table/
     :alt: Updates



A tool for converting traditional shipwrights offset tables for defining boat hulls into electronic forms


* Free software: MIT license
* Documentation: https://lines-table.readthedocs.io.


Features
--------

This project is a tool that generate a 3D model of a ship's hull given a table of points in the form of a traditional shipwright's offset or lines table. These tables contain, in theory, all the information needed to model a ship's hull, importing these individual points using 3D modeling tools can be tedious. This project aims to help with that.

Two drawing applications are the target for this project: OpenSCAD and Fusion 360. OpenSCAD is designed to define objects grammatically, so seems like a good first step, but has limited ability to handle curves. Fusion 360 includes 3D modeling and design tools with API for both Python and C++. While these can be challenging to use, they unlock a rich array of design features.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
