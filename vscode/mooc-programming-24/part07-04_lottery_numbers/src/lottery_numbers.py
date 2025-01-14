# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    """
    Generates a list of unique random numbers within a specified range,
    sorted in ascending order.

    Args:
        amount (int): The number of random numbers to generate.
        lower (int): The lower bound of the range (inclusive).
        upper (int): The upper bound of the range (inclusive).
    
    Returns:
        list[int]: A list of unique random numbers sorted in ascending order.
    """
    if amount > (upper - lower + 1):
        raise ValueError("The range is too small to generate the required amount of unique numbers.")
    
    numbers = random.sample(range(lower, upper + 1), amount)
    return sorted(numbers)