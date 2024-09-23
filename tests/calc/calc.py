#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------
# Phantom sample App Connector python file
# -----------------------------------------

# Phantom App imports
import phantom.app as phantom
from phantom.action_result import ActionResult
from phantom.base_connector import BaseConnector

from phtoolbox.app.base_connector import (
    NiceBaseConnector,
    handle,
)


class CalcConnector(BaseConnector, NiceBaseConnector):
    def __init__(self):
        BaseConnector.__init__(self)
        NiceBaseConnector.__init__(
            self, phantom.APP_SUCCESS, phantom.APP_ERROR)

    def handle_action(self, param):
        # handle_action is an abstract method; it MUST be implemented here.
        self.nice_handle_action(param)

    @handle('add')
    def _handle_add(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        return action_result.set_status(phantom.APP_SUCCESS,
                                        f"Sum {self.x + self.y}")

    @handle('subtract')
    def _handle_subtract(self, param):
        action_result = self.add_action_result(ActionResult(dict(param)))

        return action_result.set_status(phantom.APP_SUCCESS,
                                        f"Difference {self.x - self.y}")

    def initialize(self):
        ret = super(CalcConnector, self).initialize()
        config = self.get_config()

        self.x = config['x']
        self.y = config['y']

        return ret
