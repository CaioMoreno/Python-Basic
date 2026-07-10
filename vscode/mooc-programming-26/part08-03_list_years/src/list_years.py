# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date

def list_years(dates: list):
    years=[]
    for i in range (len(dates)):
        years.append(dates[i].year)
    years.sort()
    return years

