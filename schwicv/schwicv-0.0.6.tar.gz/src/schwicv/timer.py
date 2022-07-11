import datetime


class Timer:

    def __init__(self, target_time: float):
        self.__start_time = datetime.datetime.now()
        self.__set_time = target_time

    def start_ms(self, target_time: float):
        self.__start_time = datetime.datetime.now()
        self.__set_time = target_time

    # Property time over - Start time defined with start_ms
    def __get_time_over(self) -> bool:
        elapsed_time = datetime.datetime.now() - self.__start_time
        return elapsed_time.microseconds / 1000 >= self.__set_time

    time_over = property(__get_time_over, doc="Returns true if time is over")

    # Property Get Time Stamp of Start Time
    def __get_time_stamp(self) -> datetime.datetime:
        return datetime.datetime.now()

    time_stamp = property(__get_time_stamp, doc="Returns actual time stamp")

    # Property Get Time Stamp of Start Time as String
    def __get_time_stamp_str(self) -> str:
        time = datetime.datetime.now()
        output = time.strftime("%Y%m%d-%H%M%S-%f")
        return output

    time_stamp_str = property(__get_time_stamp_str, doc="Returns Actual time stamp, example: 20210708-075514-612456 "
                                                        "yearmonthday-hhmmss-µs")

    # Property Execution Time as datetime.timedelta
    def __get_execution_time(self) -> datetime.timedelta:
        return datetime.datetime.now() - self.__start_time

    execution_time = property(__get_execution_time, doc="Returns execution time since last start")

    # Property Execution Time ms as float
    def __get_execution_time_ms(self) -> float:
        return self.execution_time.microseconds / 1000

    execution_time_ms = property(__get_execution_time_ms, doc="Returns execution time in ms since last start")

    def __get_remaining_time_ms(self) -> float:
        execution_time_ms = self.__get_execution_time_ms()
        if self.__set_time > execution_time_ms:
            remaining_time_ms = self.__set_time - execution_time_ms
        else:
            remaining_time_ms = 0
        return remaining_time_ms

    remaining_time_ms = property(__get_remaining_time_ms, doc="Returns remaining time in ms since last start")

    def __get_remaining_percent(self) -> float:
        remaining_time_ms = self.__get_remaining_time_ms()
        if remaining_time_ms > 0:
            remaining_percent = remaining_time_ms / self.__set_time * 100
        else:
            remaining_percent = 0
        return remaining_percent

    remaining_percent = property(__get_remaining_percent, doc="Returns remaining time in percent since last start")

