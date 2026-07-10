# Write your solution here
from datetime import *

day=int(input('Day: '))
month=int(input('Month: '))
year=int(input('Year: '))

born=datetime(year, month, day)
mil=datetime(2000, 1, 1)

dif=mil-born

if dif.days>0:
    print(f'You were {dif.days-1} days old on the eve of the new millennium.')
else:
    print("You weren't born yet on the eve of the new millennium.")