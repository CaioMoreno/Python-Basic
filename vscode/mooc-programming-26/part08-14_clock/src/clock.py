# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour=hour
        self.minute=minute
        self.second=second

    def tick(self):
        self.second+=1
        if self.second==60:
            self.second=0
            self.minute+=1
        if self.minute==60:
            self.minute=0
            self.hour+=1
        if self.hour==24:
            self.hour=0

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
        
    def set(self, set_hour: int, set_minute: int):
        self.hour=set_hour
        self.minute=set_minute
        self.second=0

