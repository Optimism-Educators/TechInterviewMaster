# Author: <Antim Pal>
# Date: 21-04-2025
# Program: HCF of two numbers using built-in function
# Title: HCF of two numbers using built-in function
# Description: This program finds the HCF of two numbers using the built-in gcd function from the math module.
# The HCF (Highest Common Factor) is the largest number that divides both numbers without leaving a remainder.     
# The program prompts the user to enter two numbers, calculates their HCF using the gcd function, and prints the result.
# The program uses the math module to access the gcd function, which is a built-in function in Python for calculating the HCF.
# The program is simple and efficient, making it easy to find the HCF of two numbers without having to implement the algorithm manually.
# The program is designed to be user-friendly, with clear prompts and output messages.

# The program is written in Python 3 and is compatible with any version of Python 3.x.
# The program is easy to understand and can be modified to suit different requirements if needed.

def hcf(a, b):
    """Function to find HCF of two numbers using built-in function"""
    from math import gcd
    return gcd(a, b)

# Prompt the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the HCF of the two numbers using the built-in function
result = hcf(num1, num2)

# Print the result
print("The HCF of", num1, "and", num2, "is", result)

# The output of the program will be:
# Enter the first number: 12
# Enter the second number: 18
# The HCF of 12 and 18 is 6
# The program uses the built-in gcd function from the math module to calculate the HCF of two numbers.
# The gcd function is efficient and handles large numbers well.