import math

def arithmetic_sequence(start: float, step: float, count: int):
    return [start + i * step for i in range(count)]

def geometric_sequence(start: float, ratio: float, count: int):
    return [start * (ratio ** i) for i in range(count)]

def fibonacci_sequence(count: int):
    sequence = [0, 1]
    while len(sequence) < count:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:count]

def factorial_number(n: int):
    return math.factorial(n)

def prime_sequence(count: int):
    primes = []
    num = 2
    while len(primes) < count:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes


def triangular_sequence(count: int):
    return [int((n * (n + 1)) / 2) for n in range(1, count + 1)]

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
