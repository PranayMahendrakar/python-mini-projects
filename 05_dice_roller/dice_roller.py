"""Dice Roller - Roll multiple dice"""
import random

def roll_dice(num_dice=1, sides=6):
      return [random.randint(1, sides) for _ in range(num_dice)]

if __name__ == "__main__":
      print("=== Dice Roller ===")
      while True:
                try:
                              num = int(input("Number of dice (or 0 to quit): "))
                              if num == 0: break
                                            sides = int(input("Sides per die: "))
                              results = roll_dice(num, sides)
                              print(f"Results: {results}, Total: {sum(results)}")
except ValueError:
            print("Invalid input")
