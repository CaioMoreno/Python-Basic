# Write your solution here
number = int(input("How many items: "))

list=[]

for i in range(number):
    item = int(input(f"Item {i + 1}: "))
    list.append(item)

print(list)