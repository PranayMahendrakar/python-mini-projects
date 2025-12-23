"""
Simple Calculator
Performs basic arithmetic operations
"""

def add(x, y):
      return x + y

def subtract(x, y):
      return x - y

def multiply(x, y):
      return x * y

def divide(x, y):
      if y == 0:
                return "Error: Division by zero"
            return x / y

def calculator():
      print("=== Simple Calculator ===")
    print("Operations: +, -, *, /")

    while True:
              try:
                            num1 = float(input("Enter first number (or 'q' to quit): "))
except ValueError:
            print("Goodbye!")
            break

        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operation == '+':
                      print(f"Result: {add(num1, num2)}")
elif operation == '-':
            print(f"Result: {subtract(num1, num2)}")
elif operation == '*':
            print(f"Result: {multiply(num1, num2)}")
elif operation == '/':
            print(f"Result: {divide(num1, num2)}")
else:
            print("Invalid operation")
          print()

if __name__ == "__main__":
      calculator()
