# write your solution here
def read_fruits():
    dictionary={}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            key=line.split(';')
            name=key[0]
            price=float(key[1])
            dictionary[name]=price
    return dictionary