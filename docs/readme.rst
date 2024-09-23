Phantom Toolbox is library intended to simplify the development of
Splunk SOAR Applications using modern software development techniques.
This is an alpha release.

This product is supported by the Cybersecurity Development team at the
University of Illinois, on a best-effort basis. The expected End-of-Life
and End-of-Support dates of this version are October of 2028, the same as
its primary dependencies: `Python V3.12 <https://peps.python.org/pep-0693/>`_.

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

Usage
=====

The following `__init__` and `handle_action` boilerplate are required:

```python
class ExampleConnector(BaseConnector, NiceBaseConnector):
    def __init__(self):
        BaseConnector.__init__(self)
        NiceBaseConnector.__init__(
            self, phantom.APP_SUCCESS, phantom.APP_ERROR)

    def handle_action(self, param):
        # handle_action is an abstract method; it MUST be implemented here.
        self.nice_handle_action(param)
```

The decorator `@handle` is used to register a handler to process an action:

```python
    @handle('add')
    def _handle_add(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        return action_result.set_status(phantom.APP_SUCCESS,
                                        f"Sum {self.x + self.y}")
```
