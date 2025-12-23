"""
Rock Paper Scissors Game
"""
import random

def play_game():
      choices = ['rock', 'paper', 'scissors']
      while True:
                player = input("Enter rock, paper, scissors (q to quit): ").lower()
                if player == 'q':
                              break
                          if player not in choices:
                                        print("Invalid!")
                                        continue
                                    computer = random.choice(choices)
                print(f"Computer: {computer}")
                if player == computer:
                              print("Tie!")
elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            print("You win!")
else:
            print("Computer wins!")

if __name__ == "__main__":
      play_game()
