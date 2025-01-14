from fractions import Fraction

def fractionate(amount: int):
    """
    Divides the number 1 into `amount` equal-sized fractions.
    
    Args:
        amount (int): The number of parts to divide 1 into.
        
    Returns:
        list[Fraction]: A list of fractions representing the parts.
    """
    if amount <= 0:
        raise ValueError("The amount must be a positive integer.")
    fraction = Fraction(1, amount)  # Create a fraction of 1 divided by the given amount
    return [fraction] * amount      # Return a list containing the fraction repeated `amount` times

