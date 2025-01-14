# Write your solution here
list = []
word = input("Word: ")
while True:
    if word in list:
        break
    else:
        list.append(word)
        word = input("Word: ")

count = len(list)        
print(f"You typed in {count} different words")