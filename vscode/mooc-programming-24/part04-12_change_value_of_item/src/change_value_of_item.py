# Write your solution here

list = [1, 2, 3, 4, 5]

index = int(input("Index: "))
while index != -1:
    newv = int(input("New value: "))
    list[index] = newv
    print (list)
    index = int(input("Index: "))