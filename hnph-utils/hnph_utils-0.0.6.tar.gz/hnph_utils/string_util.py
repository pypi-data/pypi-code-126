import random
import string


class StringUtil:
    @staticmethod
    def random_string(str_length: int) -> str:
        """
        生成随机字符串
        :param str_length: 需要生成随机字符串的长度
        :return:
        """
        return ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, str_length))
