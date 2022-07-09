import hashlib


class EncryptionUtil:
    @staticmethod
    def md5(s: str) -> str:
        """
        将字符串进行MD5加密
        :param s: 需要加密的字符串
        :return: 32位的加密后的字符串
        """
        return hashlib.md5(s.encode()).hexdigest().upper()

    @staticmethod
    def sha256(s: str) -> str:
        """
        将字符串进行SHA256加密
        :param s: 需要加密的字符串
        :return: 64位的加密后的字符串
        """
        return hashlib.sha256(s.encode()).hexdigest().upper()
