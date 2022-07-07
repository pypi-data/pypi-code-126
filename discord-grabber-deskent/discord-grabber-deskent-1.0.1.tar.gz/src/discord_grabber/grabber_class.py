import json
from random import randint, choice
from base64 import b64encode
from typing import Tuple, Dict

import requests
from python3_anticaptcha import HCaptchaTaskProxyless
from fake_useragent import UserAgent
from myloguru.my_loguru import get_logger
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    ANTICAPTCHA_KEY: str
    WEB_URL: str
    EMAIL: EmailStr
    PASSWORD: str
    DEBUG: bool


class UserModel(BaseModel):
    email: EmailStr
    password: str


settings = Settings(_env_file='../../.env', _env_file_encoding='utf-8')
level = 1 if settings.DEBUG else 20
logger = get_logger(level)


class TokenGrabber:
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

    def __init__(
            self, email: str, password: str, requests_proxy: dict = None, aiohttp_proxies: str = ''
    ):
        user = UserModel(email=email, password=password)
        self.email: EmailStr = user.email
        self.password: str = user.password
        self.user_agent: str = UserAgent()['google chrome']
        self.session: requests.Session = requests.Session()
        self.fingerprint: str
        self.requests_proxy: dict = requests_proxy if requests_proxy else {}
        self.aiohttp_proxies: str = aiohttp_proxies

    def get_token(self) -> Dict[str, str]:
        self._update_headers()
        self._update_fingerprint()
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

    def _update_fingerprint(self, params: dict = None):
        logger.debug("Getting fingerprint...")
        if params is None:
            params = {
                'url': "https://discord.com/api/v9/experiments",
                'verify': False
            }
        try:
            r = self.session.get(**params)
            self.fingerprint = json.loads(r.text)["fingerprint"]
            logger.success("Getting fingerprint...OK")
        except KeyError as err:
            logger.exception(f'Getting fingerprint...FAIL: {err}')
            raise

    def _get_token_data(self) -> dict:
        logger.debug("Getting token...")
        response_text, _ = self._authenticate()
        if 'token' in response_text:
            logger.success("Getting token...OK")
            return json.loads(response_text)
        elif 'captcha_sitekey' in response_text:
            logger.debug(f'Капча для {self.email}, отправляю запрос на решение')
            return self._get_captcha(response_text)
        elif 'The resource is being rate limited' in response_text:
            logger.error('Рейт-лимит')
            return {'result': 'rate limit'}
        elif 'ACCOUNT_LOGIN_VERIFICATION_EMAIL' in response_text:
            logger.error(f'Требуется подтверждение по почте для {self.email}')
            return {'result': 'email secure'}
        else:
            logger.error('Ошибка во время решения капчи')
            return {'result': 'captcha error'}

    def _get_xsuperproperties(self) -> bytes:
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

    def _authenticate(self, captcha_key: str = '') -> Tuple[str, int]:
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
        status_code = response.status_code
        if status_code == 200:
            logger.success("Authenticating...OK")
        else:
            logger.error(f"Authenticating...FAIL: {status_code}")
        return response.text, status_code

    def _get_captcha(self, response_text: str) -> Dict[str, str]:
        logger.debug("Getting captcha...")
        captcha_sitekey: str = json.loads(response_text)['captcha_sitekey']
        result: dict = (
            HCaptchaTaskProxyless
            .HCaptchaTaskProxyless(anticaptcha_key=settings.ANTICAPTCHA_KEY)
            .captcha_handler(websiteURL=settings.WEB_URL, websiteKey=captcha_sitekey)
        )
        logger.debug('Ответ от капчи пришел.')
        captcha_key = result.get('solution', {}).get('gRecaptchaResponse', '')

        if not captcha_key:
            logger.error("Getting captcha...FAIL")
            return {"result": 'Account authorization key not found in the system'}
        logger.success("Getting captcha...OK")
        response_text, status_code = self._authenticate(captcha_key)
        if status_code == 200:
            logger.success("Getting token...OK")
            return json.loads(response_text)
        else:
            logger.error(f'Невалидная комбинация для {self.email}:{self.password}')
            return {'result': 'invalid email or password'}
