# Write your solution here
def factorials(n: int):
    dictionary={}
    for i in range(1,n+1):
        valor=1
        for j in range(i,0,-1):
            valor=valor*j
        dictionary[i]=valor
    return dictionary
