# Write your solution here

def distinct_numbers(list):
    tam = len(list)
    listorder = []
    
    for i in range(tam):
        tam2 = len(listorder)
        ver = 0
        for j in range(tam2):
            if list[i]==listorder[j]:
                ver=1
                break

        if ver == 0:
            listorder.append(list[i])
        else:
            continue
    listorder.sort()
    return listorder

