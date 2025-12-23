"""Hangman Game"""
import random
words = ["python", "programming", "computer", "developer", "algorithm"]
word = random.choice(words)
guessed = set()
tries = 6

while tries > 0:
      display = "".join(c if c in guessed else "_" for c in word)
      print(f"\n{display} (Tries: {tries})")
      if "_" not in display:
                print("You won!")
                break
            guess = input("Guess: ").lower()
    if guess in word:
              guessed.add(guess)
else:
        tries -= 1
else:
    print(f"Game over! Word: {word}")
