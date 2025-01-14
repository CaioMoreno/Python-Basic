# Write your solution here
def length_of_longest(list):
    tam = len(list)
    var=""
    for i in range(tam):
        if len(list[i])>len(var):
            var=list[i]
    return len(var)


