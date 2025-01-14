# Write your solution here
from random import *

def roll(die: str):
    if die=='A':
        sides=[3, 3, 3, 3, 3, 6]
    elif die=='B':
        sides=[2, 2, 2, 5, 5, 5]
    else:
        sides=[1, 4, 4, 4, 4, 4]
    shuffle(sides)
    return sides[0]

def play(die1: str, die2: str, times: int):
    w1=0
    w2=0
    draw=0
    for i in range(times):
        d1=roll(die1)
        d2=roll(die2)

        if d1>d2:
            w1+=1
        elif d2>d1:
            w2+=1
        else:
            draw+=1
    results=(w1, w2, draw)
    return results

