# Author: <Antim PAl>
# Date: <21-04-2025>
# Program to calculate the factorial of a number using recursion
# Description: This program calculates the factorial of a number using recursion.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# It is denoted by n! and is defined as:
# n! = n * (n-1) * (n-2) * ... * 1
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
# The factorial of 0 is defined to be 1.
# The program takes a number as input and calculates its factorial using a recursive function.
# The recursive function calls itself with a decremented value of n until it reaches the base case of n = 0.
# The base case returns 1, and the recursive calls return the product of n and the factorial of (n-1).
# The final result is printed to the console.
# The program handles invalid input by checking if the input is a non-negative integer.
# If the input is invalid, an error message is displayed.
# The program is written in Python and uses a simple recursive function to calculate the factorial.

def factorial(n):
     # Base case: if n is 0, return 1x
     if n == 0:
          return 1
     # Recursive case: n! = n * (n-1)!
     else:
          return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a non-negative integer: "))

# Check if the input is a non-negative integer
if num < 0:
     print("Error: Input must be a non-negative integer.")
else:
     # Calculate the factorial of the input number using the recursive function
     result = factorial(num)
     # Print the result
     print("The factorial of", num, "is", result)
     
     
# The program calculates the factorial of a number using recursion.
# It takes a non-negative integer as input and returns the factorial of that number.
# The program uses a recursive function to calculate the factorial.
# The base case is when n is 0, in which case the function returns 1.
# For any other positive integer n, the function returns n multiplied by the factorial of (n-1).
# The program handles invalid input by checking if the input is a non-negative integer.
# If the input is invalid, an error message is displayed.
# The program is user-friendly and provides clear instructions for input.
# The program is written in Python and uses a simple recursive function to calculate the factorial.
# The program is designed to be user-friendly and provides clear instructions for input.
# The program is also well-documented with comments to explain the code.
# Overall, this program is a simple and effective way to calculate the factorial of a number using recursion in Python.