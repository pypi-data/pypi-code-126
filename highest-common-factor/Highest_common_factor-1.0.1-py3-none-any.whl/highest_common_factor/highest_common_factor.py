'''
Contains the highest common factor function.

This module provides a function that you want to use if you want to get the highest common factor of a number.

'''


def get_highest_common_factor(*numbers):
    ''' 
    Returns the highest common factor of all the numbers typed into *numbers.

    Parameters:
    *numbers (iterable): the list of numbers

    Returns:
    int: The highest common factor of all the numbers.
    '''
    factors = []
    for number in numbers:
        for potential_factor in range(1, number+1):
            if number % (potential_factor) == 0:
                factors.append(potential_factor)
    return max([factor for factor in factors if factors.count(
        factor) == len(numbers)])
