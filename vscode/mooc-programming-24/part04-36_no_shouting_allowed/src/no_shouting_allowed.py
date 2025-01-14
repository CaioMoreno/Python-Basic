# Write your solution here
def no_shouting(list):
    tam=len(list)
    list2=[]
    for i in range(tam):
        if list[i].isupper()==False:
            list2.append(list[i])
    return list2
