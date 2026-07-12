# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers=numbers

    def number_of_hits(self, numbers: list):
        return len([n for n in self.numbers if n in numbers])
    
    def hits_in_place(self, numbers: list):
        return [n if n in self.numbers else -1 for n in numbers]

