
# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        lenght=0
        for line in new_file:
            n=int(line)
            if lenght<n:
                lenght=n
    return lenght