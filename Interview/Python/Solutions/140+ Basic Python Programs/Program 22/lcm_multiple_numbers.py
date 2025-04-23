# Author: <Anitm Pal>
# Date: <2025-04-21>
# Title: LCM of Multiple Numbers
# Description: Write a Python program to find the LCM of multiple numbers.
# The program should take a list of numbers as input and return the LCM of those numbers.
# The LCM of two numbers a and b can be calculated using the formula:
# LCM(a, b) = abs(a*b) / GCD(a, b)
# where GCD is the greatest common divisor.
# To find the LCM of multiple numbers, we can use the following approach:
# 1. Initialize the LCM to the first number in the list.
# 2. Iterate through the list of numbers starting from the second number.
# 3. For each number, update the LCM using the formula:
#    LCM = (LCM * number) / GCD(LCM, number)
# 4. Return the final LCM.
# 5. The GCD can be calculated using the Euclidean algorithm.
# 6. The Euclidean algorithm is a method for computing the greatest common divisor (GCD) of two numbers.
# 7. The algorithm is based on the principle that the GCD of two numbers also divides their difference.
# 8. The algorithm can be implemented using recursion or iteration.
# 9. The base case for the recursion is when one of the numbers is zero, in which case the GCD is the other number.
# 10. The recursive case is to call the function with the second number and the remainder of the first number divided by the second number.
# 11. The algorithm can be implemented using a while loop or a for loop.
# 12. The while loop continues until one of the numbers becomes zero, at which point the other number is returned as the GCD.
# 13. The for loop continues until the second number becomes zero, at which point the first number is returned as the GCD.
# 14. The GCD can be calculated using the built-in math.gcd function in Python.
# 15. The math.gcd function takes two numbers as input and returns their GCD.
# 16. The GCD can be calculated using the Euclidean algorithm.
# 17. The Euclidean algorithm is a method for computing the greatest common divisor (GCD) of two numbers.
# 18. The algorithm is based on the principle that the GCD of two numbers also divides their difference.
# 19. The algorithm can be implemented using recursion or iteration.
# 20. The base case for the recursion is when one of the numbers is zero, in which case the GCD is the other number.
# 21. The recursive case is to call the function with the second number and the remainder of the first number divided by the second number.

def gcd(a, b):
     """Calculate the GCD of two numbers using the Euclidean algorithm."""
     while b:
          a, b = b, a % b
     return a
def lcm_multiple_numbers(numbers):
     """Calculate the LCM of multiple numbers using the Euclidean algorithm."""
     lcm = numbers[0]
     for number in numbers[1:]:
          lcm = lcm * number // gcd(lcm, number)
     return lcm

# Test the function with a list of numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
lcm = lcm_multiple_numbers(numbers)
print("LCM of", numbers, "is", lcm)