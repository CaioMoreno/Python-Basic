# Write your solution here
list = []
print(f"The list is now {list}")
option = input("a(d)d, (r)emove or e(x)it: ")
i=0
while option != 'x':
    if option == 'd':
        list.insert(i, i+1)
        i+=1 
    elif option == 'r':
        list.remove(i)
        i-=1
    print(f"The list is now {list}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    

print("Bye!")