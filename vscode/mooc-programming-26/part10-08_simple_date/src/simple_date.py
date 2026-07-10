# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __ne__(self, value):
        return self.day != value.day or self.month != value.month or self.year != value.year

    def __eq__(self, value):
        return self.day == value.day and self.month == value.month and self.year == value.year

    def __lt__(self, other):
        date1 = self.year + self.month*0.1 + self.day*0.01
        date2 = other.year + other.month*0.1 + other.day*0.01
        return date1 < date2

    def __gt__(self, other):
        date1 = self.year + self.month*0.1 + self.day*0.01
        date2 = other.year + other.month*0.1 + other.day*0.01
        return date1 > date2
    
    def __add__(self, day):
        years=day//360+self.year
        day%=360
        months=day//30+self.month
        day%=30
        days=day+self.day
        if days>30:
            days-=30
            months+=1
        if months>12:
            months-=12
            years+=1
        
        return SimpleDate(days, months, years)
    
    def __sub__(self, other):
        years=self.year-other.year
        months=self.month-other.month
        days=self.day-other.day

        total_dif=(years*360)+(months*30)+(days)

        return abs(total_dif)
    
