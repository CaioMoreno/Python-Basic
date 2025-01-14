# Write your solution here
def longest_series_of_neighbours(list):
    aux=list[0]
    tam=len(list)
    n=1
    n1=1
    for i in range(1, tam):
        if aux == list[i]-1 or aux==list[i]+1:
            n+=1
        else:
            if n1<n:
                n1=n
            n=1
        aux=list[i]
    if n > n1:
        n1 = n
    return n1

