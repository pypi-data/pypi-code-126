import datetime

YYYY_MM_DD = '%Y-%m-%d'
YYYY_MM_DD_HH_MI_SS = '%Y-%m-%d %H:%M:%S'


class DateUtil:
    """
    日期处理工具类
    """
    @staticmethod
    def now_date() -> datetime.date:
        """
        获取当前系统日期
        :return:
        """
        return datetime.date.today()

    @staticmethod
    def now_datetime() -> datetime:
        """
        获取当前系统时间
        :return:
        """
        return datetime.datetime.now()

    @staticmethod
    def date_to_str(d, fmt=YYYY_MM_DD) -> str:
        """
        将日期转换为字符串格式输出
        :param d: 需要转换的日期对象
        :param fmt: 转换后的格式
        :return:
        """
        return d.strftime(fmt)

    @staticmethod
    def str_to_date(s, fmt=YYYY_MM_DD) -> datetime.date:
        """
        字符串转换成日期
        :param s: 日期格式的字符串
        :param fmt: 格式 YYYY-MM-DD
        :return:
        """
        return datetime.datetime.strptime(s, fmt).date()

    @staticmethod
    def datetime_to_str(dt, fmt=YYYY_MM_DD_HH_MI_SS) -> str:
        """
        将日期转换为字符串格式输出
        :param dt: 需要转换的日期对象
        :param fmt: 转换后的格式
        :return:
        """
        return dt.strftime(fmt)

    @staticmethod
    def str_to_datetime(s, fmt=YYYY_MM_DD_HH_MI_SS) -> datetime.datetime:
        """
        将日期格式的字符串转换成日期时间格式对象
        :param s: 字符串格式的日期时间
        :param fmt: 格式 YYYY-MM-DD HH:mm:ss
        :return:
        """
        return datetime.datetime.strptime(s, fmt)

    @staticmethod
    def this_month_begin_time() -> datetime.datetime:
        """
        当前月份开始时间
        :return:
        """
        return datetime.datetime.strptime(DateUtil.now_datetime().strftime('%Y-%m') + '-01 00:00:00', YYYY_MM_DD_HH_MI_SS)
