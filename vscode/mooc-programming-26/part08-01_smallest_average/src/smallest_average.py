# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    c1=(person1["result1"]+person1["result2"]+person1["result3"])/3
    c2=(person2["result1"]+person2["result2"]+person2["result3"])/3
    c3=(person3["result1"]+person3["result2"]+person3["result3"])/3

    smallest=min(c1, c2, c3)

    if c1==smallest:
        return person1
    elif c2==smallest:
        return person2
    else:
        return person3
