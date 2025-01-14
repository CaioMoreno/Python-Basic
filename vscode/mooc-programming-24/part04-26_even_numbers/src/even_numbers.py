# Write your solution here
def even_numbers(list):
    tam = len(list)
    list2 = []
    for i in range(tam):
        if list[i]%2 == 0:
            list2.append(list[i])
        else:
            continue
    return list2