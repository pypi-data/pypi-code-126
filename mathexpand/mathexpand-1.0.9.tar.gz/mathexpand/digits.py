def take_digits(number):
    digits = list()
    temp = number

    for i in range(len(str(number)) - 1):
        divisor = int("1" + (len(str(temp))-1) * "0")
        digits.append(int((temp - temp % divisor) / divisor))

        temp = temp % divisor

    digits.append(temp)

    return digits

# print(take_digits(356486))
# print(take_digits(6743526582638753426723483258236542836247356398))
