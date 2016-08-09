#!/usr/bin/env python

import unittest
import ConfigParser
import tempfile
import os
from mock import patch
from cStringIO import StringIO

import notifypush


class NotifyPushTest(unittest.TestCase):
    def setUp(self):
        notifypush.config = ConfigParser.ConfigParser()
        self.tempconfig = tempfile.mktemp()

    def tearDown(self):
        try:
            os.unlink(self.tempconfig)
        except:
            pass

    def test_required_options(self):
        open(self.tempconfig, 'w').write('''
[pushitbot]
        ''')
        notifypush.load_config(self.tempconfig)
        self.assertRaisesRegexp(
            notifypush.NotifyPushError,
            'Missing required option for pushitbot: token - token provided by @PushItBot',
            notifypush.push, 'oi'
        )

    def test_push(self):
        open(self.tempconfig, 'w').write('''
[pushitbot]
token = 123
        ''')
        notifypush.load_config(self.tempconfig)

        with patch('urllib2.urlopen', return_value=StringIO('{"ok": false}')):
            self.assertFalse(notifypush.push('fail'))
        with patch('urllib2.urlopen', return_value=StringIO('{"ok": true}')):
            self.assertTrue(notifypush.push('cool'))

    def test_push_fallback(self):
        open(self.tempconfig, 'w').write('''
[pushitbot]
token = 123

[notifcasterbot]
token = 321
        ''')
        notifypush.load_config(self.tempconfig)

        def _x(req):
            if req.origin_req_host == 'tgbots-fopina.rhcloud.com':
                return StringIO('{"ok": false}')
            else:
                return StringIO('{"ok": "true"}')

        with patch('urllib2.urlopen', _x):
            self.assertTrue(notifypush.push('fell back'))


if __name__ == '__main__':
    unittest.main()
