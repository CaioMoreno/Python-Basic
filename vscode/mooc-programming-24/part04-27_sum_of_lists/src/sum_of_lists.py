# Write your solution here
def list_sum(list1, list2):
    listsum=[]
    tam = len(list1)
    for i in range (tam):
        sum = list1[i]+list2[i]
        listsum.append(sum)

    return listsum