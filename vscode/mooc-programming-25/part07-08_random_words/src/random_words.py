# Write your solution here

from random import *

def words(n: int, beginning: str):
    all_words=[]
    with open("words.txt", "r") as file:
        for line in file:
            word=line.strip()
            if word.startswith(beginning):
                all_words.append(word)
    if len(all_words)<n:
        raise ValueError
        
    return sample(all_words, n)