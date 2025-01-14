# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = sample(number_pool, amount)
    order=sorted(weekly_draw)
    return order
   
