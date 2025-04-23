# Author: Antim Pal
# Date: 2025-04-21
# Sum of n natural numbers using formula
# https://www.geeksforgeeks.org/sum-n-natural-numbers-using-formula/
# Description: This program calculates the sum of the first n natural numbers using the formula n*(n+1)/2.
# The formula is derived from the arithmetic series and is a more efficient way to calculate the sum than using a loop.
# The program takes an integer input from the user and checks if it is a positive integer. If it is, it calculates the sum using the formula and prints the result. If not, it prints an error message.
# Python program to find sum of n natural numbers using formula

def sum_of_natural_numbers(n):
    # Using the formula n*(n+1)/2 to calculate the sum of first n natural numbers
    return n * (n + 1) // 2

# Get user input
n = int(input("Enter a positive integer: "))

# Check if the input is a positive integer
if n > 0:
    # Calculate the sum using the formula
    sum_result = sum_of_natural_numbers(n)
    # Print the result
    print("The sum of the first", n, "natural numbers is:", sum_result)
else:
    # Print an error message if the input is not a positive integer
    print("Error: Please enter a positive integer.")
# Output:
# Enter a positive integer: 5
# The sum of the first 5 natural numbers is: 15
# Enter a positive integer: -3
# Error: Please enter a positive integer.
# Enter a positive integer: 0
# Error: Please enter a positive integer.