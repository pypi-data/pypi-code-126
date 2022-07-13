from random import randint


def calculate_prime():
    description = (
        'Answer "yes" if given number is prime. Otherwise answer "no".')
    number = randint(1, 1000)
    i = number // 2
    result = 'yes'
    number_str = str(number)
    while i > 1:
        if number % i == 0:
            result = 'no'
        i = i - 1
    return(description, number_str, str(result))
