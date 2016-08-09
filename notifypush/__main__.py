from . import __description__, __version__, load_config, push
import argparse
import sys


def parseargs(args):

    parser = argparse.ArgumentParser(
        add_help=False,
        description=__description__,
        usage='%(prog)s [OPTIONS] message...')
    parser.add_argument(
        '-h', '--help',
        action='help',
        help=argparse.SUPPRESS)
    parser.add_argument(
        '-s', '--service',
        action='store',
        help='use only this service')
    parser.add_argument(
        '--list-services',
        action='store_true')
    parser.add_argument(
        '-c', '--config',
        action='store',
        help='use this configuration file instead of ~/.notifypush')
    parser.add_argument(
        '--version',
        action='version',
        version=__version__)
    parser.add_argument(
        'message', metavar='message',
        nargs='*', help='message')

    return parser.parse_args(args)


def main(args=None):
    opts = parseargs(args)
    if opts.list_services:
        import pkgutil
        import os
        import importlib
        for _, service, _ in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), 'services')]):
            m = importlib.import_module('.services.%s' % service, __package__).Service({}, validate=False)
            print('[%s] - %s' % (service, m.url))
            for opt in m.options:
                print('%s - %s %s' % (opt[0], opt[1], '(required)' if opt[2] else ''))
            print('')
        sys.exit(0)
    if opts.config:
        load_config(opts.config)
    if not opts.message:
        if sys.stdin.isatty():
            print('Press ctrl-D when done')
        try:
            message = sys.stdin.read()
        except KeyboardInterrupt:
            print('Cancelled')
            sys.exit(1)
    else:
        message = ' '.join(opts.message)
    if push(message, opts.service):
        print('Pushed')
    else:
        print('FAILED')
        sys.exit(1)


if __name__ == '__main__':
    main()
