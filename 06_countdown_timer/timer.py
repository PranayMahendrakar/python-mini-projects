"""Countdown Timer"""
import time

def countdown(seconds):
      while seconds > 0:
                mins, secs = divmod(seconds, 60)
                print(f"\r{mins:02d}:{secs:02d}", end="")
                time.sleep(1)
                seconds -= 1
            print("\nTime's up!")

if __name__ == "__main__":
      print("=== Countdown Timer ===")
    try:
              secs = int(input("Enter seconds: "))
              countdown(secs)
except ValueError:
        print("Invalid input")
