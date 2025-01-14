# Write your solution here
def all_the_longest(list):
    tam = len(list)
    max=0
    list2=[]
    for i in range(tam):
        if len(list[i])>max:
            max=len(list[i])
    for i in range(tam):
        if len(list[i]) == max:
            list2.append(list[i])
    return list2

