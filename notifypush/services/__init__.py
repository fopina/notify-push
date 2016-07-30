class BaseService(object):
    def __init__(self, settings):
        self.settings = type('', (), {})()
        for key, value in settings:
            setattr(self.settings, key, value)

    def push(self, message):
        raise NotImplementedError('abstract method, implement this!')
