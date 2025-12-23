"""Coin Flip"""
import random
while input("Flip? (y/n): ").lower() == 'y':
      print(random.choice(["Heads", "Tails"]))
