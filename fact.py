"""
This module has the method to calculate factorial of the given number
"""
def factorial(num):
    """ Calculates factorial of the passed number
    num (int): Integer for which factorial is requested
    returns (int): Returns Factorial
    """
    if num in (0, 1):
        return 1
    return num * factorial(num-1)
print(factorial(5))
