# Write your solution here
import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_specials: bool):
    """
    Generates a strong password with specified criteria.

    Args:
        length (int): The desired length of the password.
        include_numbers (bool): Whether to include numbers in the password.
        include_specials (bool): Whether to include special characters in the password.

    Returns:
        str: A randomly generated password meeting the criteria.
    """
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")
    
    # Define character pools
    lower_pool = string.ascii_lowercase
    number_pool = string.digits if include_numbers else ""
    special_pool = "!?=+-()#" if include_specials else ""
    
    # Ensure required characters are added
    password = [random.choice(lower_pool)]  # At least one lowercase letter
    
    if include_numbers:
        password.append(random.choice(number_pool))
    if include_specials:
        password.append(random.choice(special_pool))
    
    # Remaining length
    remaining_length = length - len(password)
    all_characters = lower_pool + number_pool + special_pool
    
    if remaining_length > 0:
        password.extend(random.choices(all_characters, k=remaining_length))
    
    # Shuffle the characters to randomize positions
    random.shuffle(password)
    
    return ''.join(password)