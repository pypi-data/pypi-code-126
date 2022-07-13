from random import randint


def calculate_numbers():
    description = 'What is the result of the expression?'
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    choice = randint(1, 3)
    choice_plus = 1
    choice_minus = 2
    if choice == choice_plus:
        result = number1 + number2
        expression_str = f'{number1} + {number2}'
    elif choice == choice_minus:
        result = number1 - number2
        expression_str = f'{number1} - {number2}'
    else:
        result = number1 * number2
        expression_str = f'{number1} * {number2}'
    return (description, expression_str, str(result))
