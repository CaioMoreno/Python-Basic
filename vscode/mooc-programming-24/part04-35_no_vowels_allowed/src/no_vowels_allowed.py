# Write your solution here
def no_vowels(string):
    tam=len(string)
    frase=""
    for i in range(tam):
        if string[i]!='a' and string[i]!='e' and string[i]!='i' and string[i]!='o' and string[i]!='u':
            frase+=string[i]

    return frase
