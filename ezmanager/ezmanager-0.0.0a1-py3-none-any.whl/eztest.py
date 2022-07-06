"""
Version - 1.0.0rc1
"""


from ez.struct import struct_value, separate
import datetime
import re

AUTO = 0

RED = (255, 60, 60)
ORANGE = (255, 120, 0)
YELLOW = (220, 200, 0)
GREEN = (0, 255, 100)
DARK_GREEN = (0, 200, 0)
PINK = (255, 90, 255)

TYPENAME_CLASS = {'auto': AUTO, 'bool': bool, 'int': int, 'float': float, 'str': str, 'list': list, 'tuple': tuple, 'dict': dict}

class EzTest:
    """
    Unittest your functions and methods by simply typing "1, 2 >>> 3"!

    Basic usage
    [I, I >>> [O, O]]

    - 1 >>> 10
    - 1, 2 >>> 3
    - 10, 20 >>> [11, 21]
    - 5 >>> [4, 3, 2, 1]

    Type setting (Select type what input/output types are)

    [# i/o type]

    - # i auto
    - # o float
    - # o int
    - # i str

    Tagging (Add tag string in log)

    [# tag TAG_MESSAGES]

    - # tag This is the way to tag in log

    Comment
    [// comment message]

    - // Type anything
    """

    def __init__(self, data_path, method, reverse=False, file_encoding='UTF8'):
        """
        Create EzTest object with a test file.

        :param data_path: dataset file's location
        :param method: target method
        :param reverse: test with reversed I/O values
        :param file_encoding: dataset file's encoding
        """
        try:
            with open(data_path, encoding=file_encoding)as f:
                self.dataset = list(map(lambda line: line.strip(), f.read().split('\n')))
        except FileNotFoundError:
            self.print_colored(f"File {data_path} does not exist. The created object may not be executed properly.")
        self.method = method
        self.reverse = reverse
        self.time = str(datetime.datetime.today())
        self.log = f"path : {data_path}    target : {method.__name__}\n" \
                   f"timestamp(object creation time) : {self.time}"
        self.input_type = AUTO
        self.output_type = AUTO


    def change_method(self, method):
        """
        Change target method.

        :param method: target method
        :return: self
        """
        self.method = method
        self.log += f"\n\nTarget changed to : {method.__name__}\n" \
                    f"timestamp : {str(datetime.datetime.today())}"
        self.print_colored(f"Target changed to : {method.__name__}", YELLOW)
        return self


    def clear_log(self):
        """
        Reset log data.

        :return: self
        """
        self.log = ""
        return self


    def start(self):
        """
        Start unittest.
        All test results (except syntax errors) will record in log.

        :return: self
        """
        self.print_colored("Test started. . .", YELLOW)
        self.log += "\n" * 2
        correct = 0
        wrong = 0
        for line in self.dataset:
            if line == "" or line[:2] == "//":  # Comment
                continue
            elif line[0] == '#':  # Command
                command = re.sub(' +', ' ', line).split(' ')[1:]
                command[0] = command[0].lower()
                if command[0] == 'i':
                    self.input_type = TYPENAME_CLASS[command[1]]
                elif command[0] == 'o':
                    self.output_type = TYPENAME_CLASS[command[1]]
                elif command[0] == 'tag':
                    self.add_tag(' '.join(command[1:]))
                continue
            elif ">>>" not in line:  # Syntax Error
                self.print_colored(f"IO divider missing -> {line}")
                continue
            i, o = '', ''
            if not self.reverse:
                i, o = map(lambda string: string.strip(), line.split(">>>"))
            else:
                o, i = map(lambda string: string.strip(), line.split(">>>"))
            i = self.cast_type(i, self.input_type)
            o = self.cast_type(o, self.output_type)

            if not (i and o):  # If None exist
                continue

            # Unpack output result because output type doesn't support enumerating >>> 1, 2, 3, 4.....
            # Right example of output writing >>> [1, 2, 3, 4]
            o = o[0]

            result = None
            i_format = str(i)[1:-1]  # i if self.input_type in [list, tuple, dict, set] else
            o_format = '\'' + o + '\'' if self.output_type == str or type(o) == str else o
            try:
                result = self.method(*i)  # if self.input_type in [list, tuple, dict, set] else self.method(*i)
                result_format = '\'' + result + '\'' if type(result) == str else result
            except Exception as e:
                self.log += f"Error : {i_format} -----> {type(e).__name__}\n"
                wrong += 1
                continue
            if result == o:
                self.log += f"Correct : {i_format} -----> {o_format}\n"
                correct += 1
            else:
                self.log += f"Wrong : {i_format} -----> {result_format}   ≠   {o_format}\n"
                wrong += 1
        self.log += f"\n\n| Test Result |\n Correct = {correct} / Wrong = {wrong}\n"
        self.print_colored("\n\n| Test Result |", YELLOW)
        self.print_colored(f"Correct = {correct}", GREEN, end='')
        print(' / ', end='')
        self.print_colored(f"Wrong = {wrong}", RED)
        print("=======================================\n")
        return self


    def cast_type(self, value, cast_to) -> list | list[list] | None:
        """
        Cast the type of value to cast_to type.

        String casting only support one parameter.
        Cannot write like this: str1, str2, str3.
        Right writing is: "str1", "str2", "str3"

        Return values in list, because EzTest unpack the input values once.
        See the process below.

        - [[v1, v2, v3]] ==Unpack=> [v1, v2, v3] (one parameter)
        - [v1, v2, v3] ==Unpack=> v1, v2, v3 (three parameters)

        :param value: String to cast into another type
        :param cast_to: A type to cast
        :return: None when error occur, a value when successfully converted
        """
        if cast_to == AUTO:
            try:
                return struct_value("["+value+"]")
            except SyntaxError as e:
                self.print_colored(e)
                self.print_colored("Test line passed", ORANGE)
        else:
            try:
                if cast_to == bool:
                    return [True] if value.lower() in [1, "true"] else [False]
                elif cast_to == str:
                    return [value]
                else:  # int, float
                    return list(map(cast_to, separate(value)))
            except ValueError:
                self.print_colored(f"Value {value} cannot be cast to '{cast_to.__name__}'")
        return None


    def save_log(self, path=''):
        def _save_log(_path=f"{self.time.split('.')[0].replace(':',';').replace(' ', '_')}.log"):
            try:
                with open(_path, 'w') as f:
                    f.write(self.log)
            except FileNotFoundError:
                self.print_colored("Invalid save path")
            pass
        _save_log(path) if path else _save_log()
        return self


    def add_tag(self, msg=''):
        """
        Add tag in log with some messages.

        e.g.)<<<<<<<<<< msg >>>>>>>>>>

        :param msg: tag message
        :return: self
        """
        self.log += f"\n<<<<<<<<<<<<<<<<<<<< {msg} >>>>>>>>>>>>>>>>>>>>\n"
        return self


    def print_log(self, colored=True):
        """
        Prints the log.
        You can color the logs by setting colored as 'True',
        but this option might affect to the performance.

        :param colored: log coloring option
        :return: self
        """
        if colored:
            for line in self.log.split('\n'):
                # TODO Try to use regex when convert these guys...
                for target, color in [('----->', PINK),
                                      ('Error ', RED),
                                      ('<<<<<<<<<<<<<<<<<<<<', DARK_GREEN),
                                      ('>>>>>>>>>>>>>>>>>>>>', DARK_GREEN),
                                      ('| Test Result |', YELLOW),
                                      ('Correct', GREEN),
                                      ('Wrong', ORANGE),
                                      ('Target changed to :', YELLOW)]:
                    color = list(map(str, color))
                    line = line.replace(target, f'\x1b[38;2;{";".join(color)}m{target}\x1b[0m')
                print(line)
        else:
            print(self.log)
        return self


    @staticmethod
    def print_colored(msg, color=RED, end='\n'):
        """
        Print message that has beautiful color into console.

        :param msg: message to print
        :param color: character color
        :param end: string appended after the last value
        """
        color = list(map(str, color))
        print(f'\x1b[38;2;{";".join(color)}m{msg}\x1b[0m', end=end)
