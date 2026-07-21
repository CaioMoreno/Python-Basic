# Write your solution here
import json

class HockeyPlayers:
    def __init__(self, players: list):
        self.__players = players

    def search(self, player: str):
        for p in self.__players:
             if p["name"] == player:
                 return p

    def teams(self):
        return sorted(set([team["team"] for team in self.__players]))

    def countries(self):
        return sorted(set([country["nationality"] for country in self.__players]))

    def team_players(self, team: str):
        player = [p for p in self.__players if p["team"] == team]
        return sorted(player, key=lambda p: p["goals"]+p["assists"], reverse=True)

    def country_players(self, country: str):
        player = [p for p in self.__players if p["nationality"] == country]
        return sorted(player, key=lambda p: p["goals"]+p["assists"], reverse=True)
    
    def most_points(self, qtt: int):
        player = [p for p in self.__players]
        player.sort(key=lambda p: p["goals"]+p["assists"], reverse=True)
        top_players = []
        for i in range(qtt):
            top_players.append(player[i])

        return top_players
        
    def most_goals(self, qtt: int):
        player = [p for p in self.__players]
        player.sort(key=lambda p: p["goals"], reverse=True)
        top_players = []
        for i in range(qtt):
            top_players.append(player[i])
        
        for i in range(1, len(top_players)):
            player1 = top_players[i-1]
            player2 = top_players[i]
            if player2["goals"] == player1["goals"]:
                if player2["games"]<player1["games"]:
                    aux = top_players[i-1]
                    top_players[i-1] = top_players[i]
                    top_players[i] = aux

        return top_players

class FileHandler:
    def __init__(self, filename: str):
        self.__filename = filename

    def load_file(self):
        with open(self.__filename) as f:
            data = f.read()
        
        players = json.loads(data)
        return players

class PlayApplication:
    def __init__(self):
        self.__filehandler = FileHandler(input("file name: "))
        self.__players = HockeyPlayers(self.__filehandler.load_file())
        print(f"read the data of {len(self.__filehandler.load_file())} players")

    
    def help(self):
        print("")
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search(self):
        name = input("name: ")
        player = self.__players.search(name)
        self.print_player(player)

    def teams(self):
        for team in self.__players.teams():
            print(team)

    def countries(self):
        for country in self.__players.countries():
            print(country)

    def team_players(self):
        team = input("team: ")
        for player in self.__players.team_players(team):
            self.print_player(player)

    def country_players(self):
        country = input("country: ")
        for player in self.__players.country_players(country):
            self.print_player(player)

    def most_points(self):
        player_qtt = int(input("how many: "))
        for player in self.__players.most_points(player_qtt):
            self.print_player(player)

    def most_goals(self):
        player_qtt = int(input("how many: "))
        for player in self.__players.most_goals(player_qtt):
            self.print_player(player)

    def print_player(self, player: dict):
        print(f"{player['name']:<21}{player['team']:>3}{player['goals']:>4} + {player['assists']:>2} = {player['goals'] + player['assists']:>3}")
   
    def execute(self):
        self.help()
        while True:
            print("")
            command = int(input("command: "))
            if command == 1:
                self.search()
            elif command == 2:
                self.teams()
            elif command == 3:
                self.countries()
            elif command == 4:
                self.team_players()
            elif command == 5:
                self.country_players()
            elif command == 6:
                self.most_points()
            elif command == 7:
                self.most_goals()
            elif command == 0:
                break
            else:
                self.help()

call = PlayApplication()
call.execute()