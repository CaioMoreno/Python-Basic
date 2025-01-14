# Write your solution here
import random
import string

def generate_password(length: int):
    """
    Generates a random password of a specified length consisting of 
    lowercase characters from 'a' to 'z'.

    Args:
        length (int): The desired length of the password.
        
    Returns:
        str: A randomly generated password.
    """
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    return ''.join(random.choices(string.ascii_lowercase, k=length))