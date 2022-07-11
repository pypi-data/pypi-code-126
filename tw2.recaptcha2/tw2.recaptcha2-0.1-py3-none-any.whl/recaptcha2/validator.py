import json

try:
    from urllib.parse import urlencode
    from urllib.request import urlopen, Request
except ImportError:
    from urllib import urlencode
    from urllib2 import urlopen
    from urllib2 import Request

from tw2.core import Validator
from tw2.core import ValidationError
from tw2.core import _


class ReCaptcha2Validator(Validator):

    required = True

    msgs = {
        'incorrect': _("Incorrect value."),
        'missing': _("Missing value."),
        'error': _("Internal error."),
    }

    def __init__(self, secret):
        super(ReCaptcha2Validator, self).__init__()
        self.secret = secret

    @property
    def remote_ip(self):
        return None

    def _validate_python(self, value, state):
        params = urlencode({
            'secret': self.secret,
            'remoteip': self.remote_ip,
            'response': value}).encode('utf-8')

        request = Request(
            url="https://www.google.com/recaptcha/api/siteverify",
            data=params,
            headers={'Content-type': "application/x-www-form-urlencoded",
                     'User-agent': "tw2.recaptcha2 Python"})

        with urlopen(request) as http_response:
            response_dict = json.loads(http_response.read().decode('utf-8'))
            if not response_dict['success']:
                error_codes = response_dict.get('error-codes', [])
                if 'invalid-input-response' in error_codes:
                    raise ValidationError('invalid')
                elif 'missing-input-response' in error_codes:
                    raise ValidationError('missing')
                else:
                    raise ValidationError('error')
