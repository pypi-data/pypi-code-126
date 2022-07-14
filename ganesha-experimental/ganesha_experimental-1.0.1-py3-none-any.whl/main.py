import random


def isPrime(n):
    # Corner case
    if n <= 1:
        return False

    # check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Function to print primes
def printPrime(n):
    previous_primes_nb = []
    for i in range(2, n + 1):
        if isPrime(i):
            previous_primes_nb.append(i)
    return previous_primes_nb


if __name__ == "__main__":
    # randomized number
    n = random.randint(2, 100)
    # function calling
    previous_primes_list = printPrime(n)
    print(previous_primes_list)
