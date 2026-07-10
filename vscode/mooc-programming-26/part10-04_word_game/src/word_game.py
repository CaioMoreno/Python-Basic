# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player1_word)<len(player2_word):
            return 2
        else:
            return 0
        
class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def count_vowels(self, word: str):
        vowels="aeiouAEIOU"
        count=0
        for c in word:
            if c in vowels:
                count+=1
        return count

    def round_winner(self, player1_word: str, player2_word: str):
        player1_points=self.count_vowels(player1_word)
        player2_points=self.count_vowels(player2_word)

        if player1_points>player2_points:
            return 1
        elif player1_points<player2_points:
            return 2
        else:
            return 0
        
class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word, player2_word):
        options={"rock", "paper", "scissors"}
        if player1_word not in options and player2_word not in options:
            return 0
        elif player1_word not in options:
            return 2
        elif player2_word not in options:
            return 1

        if player1_word==player2_word:
            return 0
        
        if player1_word==options[0] and player2_word==options[2]:
            return 1
        elif player1_word==options[1] and player2_word==options[0]:
            return 1
        elif player1_word==options[2] and player2_word==options[1]:
            return 1
        else:
            return 2


        
