"""Palindrome Checker"""
t = input("Text: ").lower().replace(" ", "")
print("Palindrome!" if t == t[::-1] else "Not palindrome")
