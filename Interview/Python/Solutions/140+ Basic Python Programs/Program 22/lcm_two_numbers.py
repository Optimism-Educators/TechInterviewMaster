# Author: <Antim Pal>
# Date: <2023-04-25>
# Program to find LCM of two numbers
# Input: Enter the first number: 12
#        Enter the second number: 18
# Output: The LCM of 12 and 18 is 36
# Explanation: The LCM of two numbers is the smallest number that is a multiple of both numbers.
# The LCM can be calculated using the formula: LCM(a, b) = (a * b) / GCD(a, b)

def gcd(a, b):
     """Function to return the GCD of two numbers"""
     while b:
          a, b = b, a % b
     return a
def lcm(a, b):
     """Function to return the LCM of two numbers"""
     return (a * b) // gcd(a, b)

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM
lcm_value = lcm(num1, num2)

# Print the result
print("The LCM of", num1, "and", num2, "is", lcm_value)

# Output: The LCM of 12 and 18 is 36
# Explanation: The LCM of two numbers is the smallest number that is a multiple of both numbers.
# The LCM can be calculated using the formula: LCM(a, b) = (a * b) / GCD(a, b)