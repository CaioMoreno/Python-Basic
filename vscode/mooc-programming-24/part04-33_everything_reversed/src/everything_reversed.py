# Write your solution here
def everything_reversed(lst):
    tam = len(lst)
    list2=[]
    for i in range(tam):
        string=lst[i]
        string=string[::-1]
        list2.append(string)
    list2=list2[::-1]
    return list2

