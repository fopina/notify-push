from .. import NotifyPushError


class BaseService(object):
    # format for service settings:
    # [(name string, help description string, required boolean)]
    # ex:
    # [
    #   ('token', 'authentication token', True),
    #   ('format', 'message format', False),
    # ]
    options = []

    def __init__(self, settings, validate=True):
        self.settings = type('', (), {})()
        for key, value in settings:
            setattr(self.settings, key, value)
        if validate:
            self.validate_settings()

    def validate_settings(self):
        for name, description, required in self.options:
            if required and not hasattr(self.settings, name):
                raise NotifyPushError('Missing required option for %s: %s - %s' % (self.name(), name, description))

    def push(self, message):
        raise NotImplementedError('abstract method, implement this!')

    def name(self):
        return self.__module__.split('.')[-1]
