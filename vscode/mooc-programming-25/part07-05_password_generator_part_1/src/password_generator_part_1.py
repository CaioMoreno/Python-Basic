# Write your solution here
from string import *
from random import *

def generate_password(amout: int):
    lowercase_letters = list(ascii_lowercase)
    shuffle(lowercase_letters)
    draw=lowercase_letters[0:amout]
    return ''.join(draw)


