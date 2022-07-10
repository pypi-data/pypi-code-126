class CaptchaTimeoutError(Exception):
    def __str__(self):
        return "Captcha time is over. Please try later..."


class CaptchaIDError(Exception):
    def __str__(self):
        return "Captcha ID error"


class RequestError(Exception):
    def __str__(self):
        return "Request error"
