# Basic Python

| Term                    | Meaning                                                   | Example                                       |
| ----------------------- | --------------------------------------------------------- | --------------------------------------------- |
| **Class**               | A blueprint/template used to create objects               | `class Person:`                               |
| **Object**              | A specific instance created from a class                  | `person1 = Person("Caio")`                    |
| **Instance**            | Another word for an object created from a class           | `person1` is an instance of `Person`          |
| **Attribute**           | A variable that belongs to an object                      | `person1.name`                                |
| **Method**              | A function that belongs to a class/object                 | `person1.say_hello()`                         |
| **Function**            | A block of reusable code (not necessarily inside a class) | `def factorial(n):`                           |
| **Constructor**         | The method that runs when creating an object (`__init__`) | `def __init__(self, name):`                   |
| **Parameter**           | A variable in a function/method definition                | `def add(x, y):` → `x` and `y` are parameters |
| **Argument**            | The actual value passed into a function/method            | `add(3, 5)` → `3` and `5` are arguments       |
| **Return value**        | The value sent back by a function                         | `return total`                                |
| **Variable**            | A name that stores a value/reference                      | `age = 22`                                    |
| **Reference**           | A variable pointing to an object in memory                | `p = Person()`                                |
| **Instance attribute**  | Attribute unique to each object                           | `self.name`                                   |
| **Class attribute**     | Attribute shared by all objects of a class                | `class Person: species = "Human"`             |
| **Private attribute**   | Attribute intended to be hidden (`__name`)                | `self.__name`                                 |
| **Getter**              | Method/property used to read a private attribute          | `def name(self): return self.__name`          |
| **Setter**              | Method/property used to modify a private attribute        | `@name.setter`                                |
| **List item / Element** | A value stored inside a list                              | `numbers[0]`                                  |
| **Dictionary key**      | The identifier used to access a dictionary value          | `"Caio"` in `{"Caio": 123}`                   |
| **Dictionary value**    | The data associated with a key                            | `123` in `{"Caio": 123}`                      |
| **Iterable**            | Something you can loop through                            | list, string, dictionary                      |
| **Loop variable**       | The temporary variable in a loop                          | `for person in people:` → `person`            |
| **Index**               | Position of an item in a sequence                         | `list[0]`                                     |
| **Inheritance**         | A class getting features from another class               | `class Dog(Animal):`                          |
| **Parent/Superclass**   | The class being inherited from                            | `Animal`                                      |
| **Child/Subclass**      | The class that inherits                                   | `Dog`                                         |
| **Composition**         | A class containing objects of another class               | `PhoneBook` contains `Person` objects         |
| **Instance method**     | A method that uses `self` and belongs to an object        | `person.name()`                               |
| **Class method**        | A method that uses `cls` and belongs to the class         | `@classmethod`                                |
| **Static method**       | A method that doesn't need object/class data              | `@staticmethod`                               |
| **Property**            | A method accessed like an attribute                       | `person.name` instead of `person.name()`      |

