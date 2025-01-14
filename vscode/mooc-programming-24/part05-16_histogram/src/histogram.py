# Write your solution here
def histogram(word: str):
    group = {}
    for letter in word:
        if letter not in group:
            group[letter]=[]
        group[letter].append('*')
    
    for key, value in group.items():
        print(f"{key} ", end='')
        for symbol in value:
            print(symbol, end='')
        print()


