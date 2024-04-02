import random
from rich import print

words = (
    "yippie",
    "rippie",
    "zippie",
    "dippie",
    "bippie",
    "nippie",
)


#Random word chosen from external file of words
#Guess's tracked => total of 5
#Each guess's(5) have 6 open spaces 
class Wordle:
    def __init__(self):
        self.word = random.choice(words)
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "]*6,
            1: [" "]*6,
            2: [" "]*6,
            3: [" "]*6,
            4: [" "]*6,
            5: [" "]*6,
        }
        
    def draw_board(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("==============================")
            
    def get_user_input(self):
        user_guess = input("Please enter a 6 letter word: ")
        while len(user_guess) != 6:
            user_guess = input("Not valid, enter a 6 letter word: ")
            
        user_guess = user_guess.lower()
        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[green]{char}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.num_guesses][idx] = char
            
        self.num_guesses += 1
        return user_guess
    
    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()
            
            if user_guess == self.word:
                self.draw_board()
                print(f"Correct! The word was {self.word}!")
                break
                
            if self.num_guesses > 5:
                self.draw_board()
                print(f"Nope :( the correct word was {self.word}...")
                break
            
game = Wordle()
game.play()