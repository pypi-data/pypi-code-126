import os
import sys


def str_is_bool(value: str) -> bool:
    if type(value) == str:
        input_str = value.lower()
        return input_str == "true" or input_str == "false"
    else:
        raise TypeError


def str_is_true(value: str) -> bool:
    if type(value) == str:
        input_str = value.lower()
        return input_str == "true"
    else:
        raise TypeError


def str_is_false(value: str) -> bool:
    if type(value) == str:
        input_str = value.lower()
        return input_str == "false"
    else:
        raise TypeError


def bool_to_str(value: bool) -> str:
    if type(value) == bool:
        if value == True:
            output_str = "True"
        else:
            output_str = "False"
        return output_str
    else:
        raise TypeError


def resource_path(relative_path) -> str:
    # So you can add directories to --onefile solution
    # And it finds the data
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("/"), relative_path)


def resource_path_test(relative_path) -> str:
    # So you can add directories to --onefile solution
    # And it finds the data
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("../"), relative_path)


def limit(value, minvalue, maxvalue):
    if (type(value) == int or type(value) == float) \
            and (type(minvalue) == int or type(minvalue) == float) \
            and (type(maxvalue) == int or type(maxvalue) == float):
        val = value
        if minvalue > maxvalue:
            raise ValueError
        if minvalue > val:
            val = minvalue
        if val > maxvalue:
            val = maxvalue
        return val
    else:
        raise TypeError
