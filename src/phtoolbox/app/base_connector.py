# -----------------------------------------
# Nice and dry Phantom App
# -----------------------------------------

import inspect


def handle(*action_ids):
    """Registor function to handle given action_ids."""
    def decorator(func):
        func._handle = action_ids
        return func
    return decorator


class NiceBaseConnector():

    def __init__(self, app_success_code, app_error_code):
        self.__version__ = 'UNSET_VERSION - set self.__version__ to emit here'
        self.__git_hash__ = \
            'UNSET_GIT_HASH - set self.__git_hash__ to emit here'
        self.__build_time__ = \
            'UNSET_BUILD_TIME - set self.__build_time__ to emit here'

        self.actions = {}
        for _, method in inspect.getmembers(self):
            if hasattr(method, '_handle'):
                for action_id in getattr(method, '_handle'):
                    self.actions[action_id] = method

        self._state = None
        self._app_success = app_success_code
        self._app_error = app_error_code

    def nice_handle_action(self, param):
        """A function to implement handle_action.
        The handle_action method MUST be defined in the child class."""
        action_id = self.get_action_identifier()
        self.debug_version_info()
        self.debug_print("action_id", self.get_action_identifier())

        if action_id in self.actions.keys():
            return self.actions[action_id](param)

        return self._app_error

    def debug_version_info(self):
        """ Developers are encouraged to set the following values:
            - self.__version__ = 'GITHUB_TAG'
            - self.__git_hash__ = 'GITHUB_SHA'
            - self.__build_time__ = 'BUILD_TIME'
        """

        self.debug_print("Version: " + self.__version__)
        self.debug_print("Git Hash: " + self.__git_hash__)
        self.debug_print("Build Time:" + self.__build_time__)

    def initialize(self):
        # Load the state in initialize, use it to store data
        # that needs to be accessed across actions
        self._state = self.load_state()
        return self._app_success

    def finalize(self):
        # Save the state, this data is saved across actions and
        # app upgrades
        self.save_state(self._state)
        return self._app_success
