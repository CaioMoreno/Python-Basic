# Write your solution here
def formatted(numbers):
    formatted_list = [] 
    for i in range(len(numbers)):
        formatted_list.append(f'{numbers[i]:.2f}') 
    return formatted_list


