from random import randint


def calculate_progression():
    description = 'What number is missing in the progression?'
    pro_length = randint(5, 10)
    pro_begin = randint(1, 100)
    pro_step = randint(1, 10)
    miss_position = randint(0, pro_length - 1)
    i = 0
    next = pro_begin
    str_accumulative = str(next)
    miss_begin = 0
    miss_end = 0 + len(str(next))
    while i <= pro_length - 1:
        if i == miss_position:
            result = str(next)
            miss_begin = len(str_accumulative) - len(str(next))
            miss_end = miss_begin + len(str(next)) - 1
        if i != pro_length - 1:
            next = next + pro_step
            str_accumulative += f' {str(next)}'
        i += 1
    progression_str = (f'{str_accumulative[:miss_begin]}..'
                       f'{str_accumulative[miss_end + 1:]}')
    return(description, progression_str, str(result))
