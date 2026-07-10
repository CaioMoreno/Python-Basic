# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.persons=[]

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return self.persons==[]

    def print_contents(self):
        print(f"There are {len(self.persons)} in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.persons==[]:
            return None
        small=self.persons[0].height
        smallest=self.persons[0]
        for person in self.persons:
            if small>person.height:
                smallest=person
                small=person.height
        return smallest
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person

