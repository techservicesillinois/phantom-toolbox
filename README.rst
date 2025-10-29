.. image:: https://github.com/techservicesillinois/phantom-toolbox/workflows/CI/CD/badge.svg
   :target: https://github.com/techservicesillinois/phantom-toolbox/actions?query=workflow%3ACI%2FCD
   :alt: Build Status

About
=====

The phantom-toolbox provides shared standardized functionality for creating and deploying Splunk SOAR applications.

This project includes:

+ A recipe for packaging a Python SOAR app and needed libraries for deployment to Splunk SOAR
+ A deploy script that can publish a SOAR app through the SOAR API
+ A nicer BaseConnector Python module that requires substantially less boilerplate code repetition

Each of these functions should work in isolation, but be aware that our own apps use all of these elements together.

End-of-Life and End-of-Support Dates
====================================

This product is supported by the Cybersecurity teams at the
University of Illinois Urbana-Champaign on a best-effort basis.

As of the last update to this README, the expected End-of-Life
and End-of-Support dates of this product are 6 November 2026.

End-of-Life was decided upon based on these dependencies:

- Python 3.13 (31 Oct 2029)
- Splunk SOAR 6.3.1 (6 November 2026)

Installation
============

For product documentation see `phantom-toolbox on PyPi <https://pypi.org/project/phantom-toolbox/>`_.
