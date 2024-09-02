#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the first command-line argument, convert it to an integer,
# and store the result of the factorial function in variable f.
f = factorial(int(sys.argv[1]))

# Print the result of the factorial calculation.
print(f)
