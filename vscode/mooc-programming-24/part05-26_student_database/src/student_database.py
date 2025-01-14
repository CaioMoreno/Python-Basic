# Write your solution here
def add_student(dictionary: dict, name: str):
    dictionary[name]=[]

def add_course(dictionary: dict, name: str, curso: tuple):
    if name in dictionary:
        if curso[1]>0:
                for c in dictionary[name]:
                    if c[0]==curso[0]:
                        if c[1]<curso[1]:
                            dictionary[name].remove(c)
                            dictionary[name].append(curso)
                        return
                dictionary[name].append(curso)

def print_student(dictionary: dict, name: str):
    media=0
    if name in dictionary:
        print(f'{name}:')
        if len(dictionary[name])>0:
            print(f' {len(dictionary[name])} completed courses:')
            for cursed, note in dictionary[name]:
                print(f'  {cursed} {note}')
                media+=note
            media=media/len(dictionary[name])
            print(f' average grade {media:.1f}')

        else:
            print(' no completed courses')
    else:
        print(f'{name}: no such person in the database')

def summary(dictionary: dict):
    print(f'students {len(dictionary)}')
    tam=0
    media2=0

    for c in dictionary:
        if len(dictionary[c])>tam:
            tam=len(dictionary[c])
            name=c
    print(f'most courses completed {tam} {name}')
    for c in dictionary:
        media1=0
        for m in dictionary[c]:
            media1+=m[1]
        media1=media1/len(dictionary[c])
        if media2<media1:
            name=c
            media2=media1
    print(f'best average grade {media2} {name}')




