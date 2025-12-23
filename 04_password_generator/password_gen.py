"""Password Generator"""
import random, string

def generate_password(length=12):
      chars = string.ascii_letters + string.digits + string.punctuation
      return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
      print("=== Password Generator ===")
      length = int(input("Length (8-50): ") or "12")
      print(f"Password: {generate_password(max(8, min(50, length)))}")
