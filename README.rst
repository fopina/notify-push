***********
notify-push
***********

.. image:: https://img.shields.io/pypi/v/notify-push.svg
    :target: https://pypi.python.org/pypi/notify-push
 
.. image:: https://img.shields.io/pypi/pyversions/notify-push.svg
    :target: https://pypi.python.org/pypi/notify-push

notify-push is a CLI tool to push notifications straight to your phone.

The usual sysadmin method is to send alerts via email but there are tons of services out there with mobile apps that allow us to send push notifications, why not use those for faster and cleaners alerts?

============
Installation
============


Simply use **pip** to install it system-wide:

.. code-block:: bash

    $ sudo pip install git+https://github.com/fopina/notify-push/

Or only for your user

.. code-block:: bash

    $ pip install --user git+https://github.com/fopina/notify-push/

=====
Usage
=====

.. code-block:: bash

    $ notify-push -h
    usage: notify-push [OPTIONS] message...

    Push notifications straight to your phone using multiple services

    positional arguments:
      message               message

    optional arguments:
      -s SERVICE, --service SERVICE
                            use only this service
      --list-services
      -c CONFIG, --config CONFIG
                            use this configuration file instead of ~/.notifypush
      --version             show program's version number and exit

Currently supported services are:

.. code-block:: bash

    $ notify-push --list-services
    notifcasterbot
    pushitbot

An example of configuration file ``~/.notifypush``:

.. code-block::

  [pushitbot]
  token = 355aac1b7f0efe055b3f2f663cae16dd

Pushing messages is now as simple as:

.. code-block:: bash

  $ notify-push hello world
  Pushed

Or using ``stdin`` (useful for shell piping):

.. code-block:: bash

  $ notify-push
  Press ctrl-D when done
  hello world
  Pushed
  $ echo hello world | notify-push
  Press ctrl-D when done
  Pushed

You can also use it easily from other python scripts:

.. code-block:: python

  >>> import notifypush
  >>> print notifypush.push('hello world')
  True
