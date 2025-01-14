# Write your solution here
item = int(input("New item: "))
list =[]
while item != 0:
    list.append(item)
    order=sorted(list)
    print(f"The list now: {list}")
    print(f"The list in order: {order}")
    item = int(input("New item: "))
print("Bye!")