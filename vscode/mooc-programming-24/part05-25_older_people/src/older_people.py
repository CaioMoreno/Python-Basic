# Write your solution here
def older_people(people: list, year: int):
    list=[]
    for p in people:
        if p[1]<year:
            list.append(p[0])
    return list

