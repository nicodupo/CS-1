def calculate_factorial(number):
    '''
    Calculates the factorial of a given number.

    Args:
        number (int): The number for which the factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.

    Raises:
        Value Error: If the input number is negative.
    '''

    if number < 0:
        raise ValueError("User error: cannot be negative!")
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i
    return factorial
