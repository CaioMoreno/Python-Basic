# Write your solution here
from json import *

def print_persons(filename: str):
    with open(filename) as my_file:
        data=my_file.read()
    
    hobby=loads(data)
    #for key, value in hobby.items():
    #    print(f"{key}: {value}")

    for value in hobby:
        print(f"{value["name"]} {value["age"]} years", end=' ')
        for key in value["hobbies"]:
            print(key, end=' ')
        print()
print_persons('file1.json')