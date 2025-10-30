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
and End-of-Support dates of this product are 29 September 2027.

Per `Splunk Software Support Policy`_, each minor release of Splunk SOAR is supported for 24 months after the release. Splunk SOAR 7.0.0 Release notes give a release date of 
29 September 2027.

.. _Splunk Software Support Policy: https://www.splunk.com/en_us/legal/splunk-software-support-policy.html

End-of-Life was decided upon based on these dependencies:

- Python 3.13 (31 October 2029) `End of Life for Python Versions`_
- Splunk SOAR 7.0.0 (29 September 2027) `Splunk SOAR 7.0.0 Release Notes`_

.. _End of Life for Python Versions: https://endoflife.date/python
.. _Splunk SOAR 7.0.0 Release Notes: https://help.splunk.com/en/splunk-soar/soar-on-premises/release-notes/7.0.0/splunk-soar-on-premises-release-notes/welcome-to-splunk-soar-on-premises-7.0.0

Installation
============

For product documentation see `phantom-toolbox on PyPi <https://pypi.org/project/phantom-toolbox/>`_.
