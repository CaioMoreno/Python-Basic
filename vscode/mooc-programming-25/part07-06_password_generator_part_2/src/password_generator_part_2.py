# Write your solution here
from string import *
from random import *


def generate_strong_password(amount: int, n: bool, s:bool):
    draw=[]
    special=['!','?','=','+','-','(',')','#']
    lowercase_letters = list(ascii_lowercase)
    shuffle(lowercase_letters)
    draw.append(lowercase_letters[0])

    if s==True:
        shuffle(special)
        draw.append(special[0])
    else:
        draw.append(lowercase_letters[1])
    if n==True:
        draw.append(randint(0, 9))
    else:
        draw.append(lowercase_letters[2])

    shuffle(draw)

    for i in range(amount-3):

        if n==True and s==True:
            wich=randint(1, 3)
        elif n==True and s==False:
            wich=randint(1, 2)
        elif n==False and s==True:
            wich=choice([1, 3])
        else:
            wich=1

        if wich==1:
            shuffle(lowercase_letters)
            draw.append(lowercase_letters[0])
        elif wich==2:
            draw.append(randint(0, 9))
        else:
            shuffle(special)
            draw.append(special[0])
    
    return ''.join(map(str, draw))

