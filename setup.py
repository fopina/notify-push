#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from setuptools import setup, find_packages
import sys

from notifypush import __program__, __version__, __description__

if sys.argv[-1] == 'pub':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'pubtest':
    os.system('python setup.py sdist upload -r https://testpypi.python.org/pypi')
    sys.exit()

README = open('README.rst').read()

# allow setup.py to be run from any path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name=__program__,
    version=__version__,
    license='MIT',
    description=__description__,
    long_description=README,
    url='https://github.com/fopina/notify-push',
    download_url='https://github.com/fopina/notify-push/tarball/v%s' %
    __version__,
    author='Filipe Pina',
    author_email='fopina@skmobi.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['notify-push=notifypush.__main__:main']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords=['push', 'notifications', 'alerts', 'messages']
)
