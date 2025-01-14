# Write your solution here
def oldest_person(people: list):
    older=people[0]
    for p in people:
        if older[1]>p[1]:
            older=p
    return older[0]


