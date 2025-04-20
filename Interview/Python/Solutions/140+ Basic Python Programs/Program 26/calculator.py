# Author: <Antim Pal>
# Date: <2023-10-05>
# Title: Simple Calculator
# Description: A simple calculator that performs addition, subtraction, multiplication, and division.
# Input: Two numbers and an operator (+, -, *, /)
# Output: The result of the operation

# Example:
# Input: 5, 3, '+'
# Output: 8
# Input: 5, 3, '-'
# Output: 2
# Input: 5, 3, '*'
# Output: 15        
# Input: 5, 3, '/'
# Output: 1.6666666666666667

def add(x, y):
    """Function to add two numbers."""
    return x + y
def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""
    if y == 0:
        return "Cannot divide by zero."
    return x / y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = input("Select operation (1/2/3/4): ")
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid Input")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == 'yes' or next_calculation.lower() == 'y':
                continue
            else:
                 print("Thank you for using the calculator.")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
    

# This program is a simple calculator that performs basic arithmetic operations.
# It allows the user to select an operation and input two numbers, then displays the result.   
# The program handles invalid inputs and division by zero errors gracefully.
# The user can perform multiple calculations in a single run.
# The program is designed to be user-friendly and easy to understand.
# The code is well-structured and follows best practices for readability and maintainability.
# The program can be easily extended to include more operations or features in the future.     
# The program is written in Python and can be run in any Python environment.
# The program is compatible with Python 3.x and should work without any issues.
