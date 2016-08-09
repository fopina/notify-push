__program__ = 'notify-push'
__version__ = '0.0.2'
__description__ = 'Push notifications straight to your phone using multiple services'

import ConfigParser
import os.path
import importlib

config = ConfigParser.ConfigParser()


def load_config(filename=None):
    if filename is None:
        filename = os.path.expanduser('~/.notifypush')
    config.read(filename)
    config._loaded = True


def push(message, module=None):
    if not hasattr(config, '_loaded'):
        load_config()

    if module is not None:
        if not config.has_section(module):
            raise NotifyPushError('No configuration found for %s' % module)
        m = importlib.import_module('.services.%s' % module, __package__)
        s = m.Service(config.items(module))
        return s.push(message)

    if not config.sections():
        raise NotifyPushError('No configuration found')

    for section in config.sections():
        m = importlib.import_module('.services.%s' % section, __package__)
        s = m.Service(config.items(section))
        if s.push(message):
            return True
    return False


class NotifyPushError(Exception):
    pass
