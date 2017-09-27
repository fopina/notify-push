from . import BaseService
import urllib2
import json


class Service(BaseService):
    url = 'http://fopina.github.io/tgbot-pushitbot/'
    options = [
        ('token', 'token provided by @PushItBot', True),
    ]

    def push(self, message):
        data = json.dumps({
            'msg': message,
        })
        req = urllib2.Request(
            'https://tgbots.skmobi.com/pushit/%s' % self.settings.token,
            data,
            {
                'Content-Type': 'application/json',
                # fake UA because of cloudflare...
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            }
        )
        try:
            f = urllib2.urlopen(req)
            response = json.loads(f.read())
            if response.get('ok', False) is True:
                return True
            else:
                return False
        except urllib2.HTTPError:
            return False
