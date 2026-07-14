# Write your solution here:
from random import choices 
def word_generator(characters: str, lenght: int, amount: int):
    return ("".join(choices(characters, k=lenght)) for i in range(amount))

 