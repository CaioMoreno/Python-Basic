# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []
        self.count = 0

    def add_number(self, number:int):
        self.numbers.append(number)
        self.count += 1

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers)==0:
            return 0
        return self.get_sum()/len(self.numbers)

all_n=NumberStats()
even_n=NumberStats()
odd_n=NumberStats()

n=0
print("Please type in integer numbers:")
while True:
    n=int(input())
    if n==-1:
        break
    all_n.add_number(n)
    if n%2==0:
        even_n.add_number(n)
    else:
        odd_n.add_number(n)

print(f"Sum of numbers: {all_n.get_sum()}")
print(f"Mean of numbers: {all_n.average()}")
print(f"Sum of even numbers: {even_n.get_sum()}")
print(f"Sum of odd numbers: {odd_n.get_sum()}")