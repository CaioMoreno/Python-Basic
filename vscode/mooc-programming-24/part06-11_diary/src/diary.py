# Write your solution here

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    choice=int(input('Function: '))

    if choice==1:
        with open("diary.txt", "a") as my_file:
            entry=input('Diary entry: ')
            my_file.write(f'{entry}\n')
            print('Diary saved')
    elif choice==2:
        with open("diary.txt", "r") as my_file:
            content = my_file.read()  
            print(content)
    else:
        print('Bye now!')
        break