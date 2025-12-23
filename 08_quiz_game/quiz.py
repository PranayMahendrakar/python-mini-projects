"""Quiz Game"""
questions = [
      {"q": "Capital of France?", "a": "paris"},
      {"q": "5 + 7 = ?", "a": "12"},
      {"q": "Color of sky?", "a": "blue"}
]

if __name__ == "__main__":
      score = 0
      for q in questions:
                if input(f"{q['q']} ").lower() == q['a']:
                              score += 1
                      print(f"Score: {score}/{len(questions)}")
