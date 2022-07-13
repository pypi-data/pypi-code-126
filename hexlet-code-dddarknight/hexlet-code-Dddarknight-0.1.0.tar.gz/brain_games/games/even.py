from random import randint


def calculate_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = randint(1, 1000)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (description, str(number), result)
