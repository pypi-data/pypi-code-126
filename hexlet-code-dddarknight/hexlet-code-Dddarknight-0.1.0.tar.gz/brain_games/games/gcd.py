from random import randint


def calculate_gcd():
    description = 'Find the greatest common divisor of given numbers.'
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    numbers_str = f'{number1} {number2}'
    minimum = min(number1, number2)
    result = 1
    while minimum >= 1:
        if (number1 % minimum == 0) and (number2 % minimum == 0):
            result = minimum
            break
        minimum -= 1
    return(description, numbers_str, str(result))
