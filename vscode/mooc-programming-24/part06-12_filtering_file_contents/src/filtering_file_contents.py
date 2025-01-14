# Write your solution here
def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()
    with open("solutions.csv", "r") as my_file:
        for line in my_file:
            parts = line.strip().split(';')
            
            if '+' in parts[1]:
                for n in parts[1]:
                    n = parts[1].split('+')
                    result=int(n[0])+int(n[1])
                if result == int(parts[2]):
                    with open("correct.csv", "a") as c_file:
                        c_file.write(f'{parts[0]};{parts[1]};{parts[2]}\n')
                else:
                    with open("incorrect.csv", "a") as i_file:
                        i_file.write(f'{parts[0]};{parts[1]};{parts[2]}\n')

            elif '-' in parts[1]:
                for n in parts[1]:
                    n = parts[1].split('-')
                    result=int(n[0])-int(n[1])
                if result == int(parts[2]):
                    with open("correct.csv", "a") as c_file:
                        c_file.write(f'{parts[0]};{parts[1]};{parts[2]}\n')
                else:
                    with open("incorrect.csv", "a") as i_file:
                        i_file.write(f'{parts[0]};{parts[1]};{parts[2]}\n')

