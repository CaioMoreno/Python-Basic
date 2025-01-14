# Write your solution here

def shortest(list):
    tam = len(list)
    var=list[0]
    for i in range(tam):
        if len(list[i])<len(var):
            var=list[i]
    return var


