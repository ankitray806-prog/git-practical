num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")
    
    choice = input("Select operation (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
Option 2: Random Password Generator
Generates a strong, customizable password using standard Python libraries.

Python
import random
import string

def generate_password(length=12):
    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage
password_len = int(input("Enter password length: "))
print(f"Generated Password: {generate_password(password_len)}")
