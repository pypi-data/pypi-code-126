def get_highest_ommon_factor(*numbers):
    factors = []
    for number in numbers:
        for potential_factor in range(1, number+1):
            if number % (potential_factor) == 0:
                factors.append(potential_factor)
    return max([factor for factor in factors if factors.count(
        factor) == len(numbers)])
