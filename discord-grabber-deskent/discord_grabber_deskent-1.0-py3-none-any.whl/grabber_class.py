import json
from random import randint, choice
from base64 import b64encode

import requests
from pydantic.annotated_types import Any
from python3_anticaptcha import HCaptchaTaskProxyless
from fake_useragent import UserAgent
from myloguru.my_loguru import get_logger
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    ANTICAPTCHA_KEY: str
    WEB_URL: str
    PASSWORD: str
    DEBUG: bool


settings = Settings(_env_file='../../.env', _env_file_encoding='utf-8')
level = 1 if settings.DEBUG else 20
logger = get_logger(level)


class TokenGrabber(BaseModel):
    """
    Класс принимает и валидирует е-мэйл и пароль от аккаунта дискорда и
    возвращает словарь с токеном, дискорд_ид и настройками дискорда.
    Автоматически проходит капчу если она требуется.

    Attributes
        email: EmailStr

        password: str
    Methods
        get_token


    """
    email: EmailStr
    password: str
    user_agent: str = None
    session: Any = None
    xsuperproperties: bytes = None
    requests_proxy: dict = None
    aiohttp_proxies: str = None
    fingerprint: str = None

    def get_token(self):
        self.user_agent = UserAgent()['google chrome']
        self.session: requests.Session = requests.Session()
        self._update_headers()
        self._get_fingerprint()
        self.session.headers.update({'X-Fingerprint': self.fingerprint})

        return self._get_token_data()

    def _update_headers(self):
        logger.debug("Getting headers...")
        self.session.headers.update(
            {'accept': '*/*', 'accept-language': 'ru,en;q=0.9', 'authorization': 'undefined',
             'content-type': 'application/json', 'origin': 'https://discord.com',
             'referer': 'https://discord.com/login', 'user-agent': self.user_agent,
             'x-super-properties': self._get_xsuperproperties()}
        )
        logger.success("Getting headers... OK")

    def _get_fingerprint(self):
        logger.debug("Getting fingerprint...")
        try:
            r = self.session.get("https://discord.com/api/v9/experiments", verify=False)
            self.fingerprint = json.loads(r.text)["fingerprint"]
            logger.success("Getting fingerprint...OK")
        except Exception as err:
            logger.exception(f'Getting fingerprint...FAIL: {err}')

    def _get_token_data(self) -> dict:
        logger.debug("Getting token...")
        response_text: str = self._authenticate()
        if 'token' in response_text:
            logger.success("Getting token...OK")
            return json.loads(response_text)
        elif 'captcha_sitekey' in response_text:
            logger.info(f'Капча для {self.email}, отправляю запрос на решение')
            captcha_key: str = self._get_captcha(response_text)
            response_text: str = self._authenticate(captcha_key)
            logger.success("Getting token...OK")
            return json.loads(response_text)
        elif 'INVALID_LOGIN' in response_text:
            logger.error(f'Невалидная комбинация для {self.email}:{self.password}')

            return {'result': 'invalid email or password'}
        elif 'The resource is being rate limited' in response_text:
            logger.error('Рейт-лимит, пробую заново')

            return {'result': 'rate limit'}
        elif 'ACCOUNT_LOGIN_VERIFICATION_EMAIL' in response_text:
            logger.error(f'Требуется подтверждение по почте для {self.email}')

            return {'result': 'email secure'}
        else:
            logger.error('Ошибка во время решения капчи, пробую заново')

            return {'result': 'captcha error'}

    def _get_xsuperproperties(self):
        xsuperproperties = {
            "os": choice(['Windows', 'Linux']), "browser": "Chrome", "device": "",
            "system_locale": choice(['ru', 'en', 'ua']), "browser_user_agent": self.user_agent,
            "browser_version": f'{randint(10, 99)}.{randint(0, 9)}.{randint(1000, 9999)}.{randint(10, 99)}',
            "os_version": choice(['xp', 'vista', '7', '8', '8.1', '10', '11']), "referrer": "",
            "referring_domain": "", "referrer_current": "", "referring_domain_current": "",
            "release_channel": "stable", "client_build_number": "10" + str(randint(1000, 9999)),
            "client_event_source": "null"
        }
        return b64encode(str(xsuperproperties).encode('utf-8'))

    def _authenticate(self, captcha_key: str = '') -> str:
        logger.debug("Authenticating...")
        data = {
            'fingerprint': self.fingerprint,
            'email': self.email,
            'password': self.password
        }
        if captcha_key:
            data.update(captcha_key=captcha_key)
        response = self.session.post(
            url='https://discord.com/api/v9/auth/login',
            json=data,
            verify=False
        )
        logger.success("Authenticating...OK")
        return response.text

    def _get_captcha(self, response_text: str):
        logger.debug("Getting captcha...")
        captcha_sitekey = json.loads(response_text)['captcha_sitekey']
        result = (HCaptchaTaskProxyless
                  .HCaptchaTaskProxyless(anticaptcha_key=settings.ANTICAPTCHA_KEY)
                  .captcha_handler(websiteURL=settings.WEB_URL, websiteKey=captcha_sitekey)
                  )
        logger.info('Ответ от капчи пришел')
        logger.success("Getting captcha...OK")
        return result['solution']['gRecaptchaResponse']


if __name__ == '__main__':
    a = TokenGrabber(email='deskent@bk.ru', password=settings.PASSWORD).get_token()
    print(a)
