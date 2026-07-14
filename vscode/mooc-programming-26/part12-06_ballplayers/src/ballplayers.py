class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals(players: list):
    player = max(players, key=lambda p: p.goals)
    return player.name

def most_points(players: list):
    player = max(players, key=lambda p: p.goals+p.passes)
    return (player.name, player.number)

def least_minutes(players: list):
    player = min(players, key=lambda p: p.minutes)
    return player

