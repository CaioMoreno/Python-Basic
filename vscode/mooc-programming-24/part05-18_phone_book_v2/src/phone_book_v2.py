# Write your solution here
book={}
while True:
    op=int(input('command (1 search, 2 add, 3 quit): '))

    if op==2:
        name=input('name: ')
        number=input('number: ')
        print('ok!')
        if name in book:
            book[name]+=number
        else:
            book[name]=number
            book[name]+='\n'

    elif op==1:
        name=input('name: ')
        if name in book:
            print(book[name])
        else:
            print('no number')

    elif op==3:
        print('quitting...')
        break
