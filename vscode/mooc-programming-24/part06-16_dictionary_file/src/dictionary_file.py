# Write your solution here
while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    n=int(input('Function:'))
    if n==1:
        wf=input('The word in Finnish: ')
        we=input('The word in English: ')
        with open('dictionary.txt', 'a') as file:
            file.write(f'{wf} - {we}\n')
        print('Dictionary entry added')
    elif n==2:
        term=input('Search term: ')
        with open('dictionary.txt') as file:
            for line in file:
                part=line.strip()
                if term in part:
                    print(part)
    else:
        print('Bye!')
        break
