class CaptchaTimeoutError(Exception):
    def __str__(self):
        return "Captcha time is over. Please try later..."


class CaptchaAPIkeyError(Exception):
    def __str__(self):
        return "Anticaptcha API key error"


class RequestError(Exception):
    def __str__(self):
        return "Request error"


class FingerPrintError(Exception):
    def __str__(self):
        return "No fingerprint got error"
