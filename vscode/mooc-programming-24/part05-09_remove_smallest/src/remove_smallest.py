# Write your solution here
def remove_smallest(numbers: list):
    small=numbers[0]
    for i in range(len(numbers)):
        if numbers[i]<small:
            small=numbers[i]
    numbers.remove(small)

