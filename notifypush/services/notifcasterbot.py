from . import BaseService
import urllib2
import json


class Service(BaseService):
    url = 'http://notifcaster.com/'
    options = [
        ('token', 'token provided by @Notifcaster_bot', True),
    ]

    def push(self, message):
        data = json.dumps({
            'api_token': self.settings.token,
            'msg': message,
        })
        req = urllib2.Request(
            'https://tg-notifcaster.rhcloud.com/api/v1/selfMessage',
            data,
            {'Content-Type': 'application/json'}
        )
        try:
            f = urllib2.urlopen(req)
            response = json.loads(f.read())
            if response.get('ok', 'false') == 'true':
                return True
            else:
                return False
        except urllib2.HTTPError:
            return False
