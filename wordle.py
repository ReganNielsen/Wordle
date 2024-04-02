import random
from rich import print

#Take random word from file
#Random word chosen from external file of words
#Guess's tracked => total of 5
#Each guess's(5) have 5 open spaces 
class Wordle:
    def __init__(self):
        self.word = random.choice(open("words_wordle.txt").readlines())
        self.num_guesses = 0
        self.guess_dict = {
            0: [" "]*5,
            1: [" "]*5,
            2: [" "]*5,
            3: [" "]*5,
            4: [" "]*5,
        }
        
    #Draw board = fill board with guesses
    def draw_board(self):
        for guess in self.guess_dict.values():
            print(" | ".join(guess))
            print("========================")
            
    #Request user input (guess), check if it is a 5 letter word 
    #Important to check input has valid characters
    def get_user_input(self):
        user_guess = input("Please enter a 5 letter word: ")
        while len(user_guess) != 5:
            user_guess = input("Not valid, enter a 5 letter word: ")
            
        #Ensure input is lower case
        #Go over/check the word in idx and input
        #If letter is correct + correct place = green
        #If letter is correct + incorrect place = yellow
        #Otherwise remain white (incorrect + incorrect place)
        user_guess = user_guess.lower()
        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"[green]{char}[/]"
                else:
                    char = f"[yellow]{char}[/]"
            self.guess_dict[self.num_guesses][idx] = char
            
        #Increase number of guess with each user guess
        self.num_guesses += 1
        return user_guess
    
    #Draw board + ask for input
    def play(self):
        while True:
            self.draw_board()
            user_guess = self.get_user_input()
            
            #If the word is guessed correctly = user wins 
            if user_guess == self.word:
                self.draw_board()
                print(f"Correct! The word was {self.word}!")
                break
                
            #If the user uses all of there guesses = user has no guesses = loses
            if self.num_guesses > 4:
                self.draw_board()
                print(f"Nope :( the correct word was {self.word}...")
                break
            
#Run game project 
game = Wordle()
game.play()