# Write your solution here
def most_common_character(string):
    tam=len(string)
    c=0
    for i in range(tam):
        cont = string.count(string[i])
        if c<cont:
            c=cont
            char=string[i]
    return char
