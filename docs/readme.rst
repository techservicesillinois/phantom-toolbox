Phantom Toolbox is library intended to simplify the development of
Splunk SOAR Applications using modern software development techniques.
This is an alpha release.

This product is supported by the Cybersecurity Development team at the 
University of Illinois, on a best-effort basis. The expected End-of-Life
and End-of-Support dates of this version are October of 2025, the same as
its primary dependencies: `Python V3.11 <https://peps.python.org/pep-0664/>`_.

.. |--| unicode:: U+2013   .. en dash
.. contents:: Jump to:
   :depth: 1

Installation
============

The simplest way to install the phantom-toolbox is to use pip.

There can be issues installing with older versions of `setuptools`, 
so we recommend ensuring setuptools is up to date before installing::

    $ pip install --upgrade setuptools
    $ pip install phantom-toolbox
