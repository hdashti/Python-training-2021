class NegativeValueForFactorialError(Exception):
    pass


def factorial(n):
    if type(n) != int:
        raise Exception
    if n < 0:
        raise NegativeValueForFactorialError(f"{n} is negative; negative values are not allowed")
    result = 1
    for i in range(1, n + 1):
        result = result * i

    return result


try:
    print(factorial(-10))
except NegativeValueForFactorialError:
    print("my plan")
