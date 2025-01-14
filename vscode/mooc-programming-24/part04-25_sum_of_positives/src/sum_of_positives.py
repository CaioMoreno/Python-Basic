# Write your solution here

def sum_of_positives (list):
    tam = len(list)
    sum = 0
    for i in range(tam):
        if list[i]>0:
            sum += list[i]
        else:
            continue
    return sum