# Write your solution here
def read_input(ask: str, n1: int, n2: int):
    while True:
        try:
            number=input(ask)
            if int(number)>=n1 and int(number)<=n2:
                return int(number)
        except ValueError:
            pass
        print(f'You must type in an integer between {n1} and {n2}')

