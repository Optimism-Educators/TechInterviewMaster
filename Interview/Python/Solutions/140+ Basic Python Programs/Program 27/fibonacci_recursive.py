# Author: <Antim Pal>
# Date: <2023-10-01>
# Description: Fibonacci series using recursion
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Note: This is not the most efficient way to calculate Fibonacci numbers, but it demonstrates recursion.
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The nth Fibonacci number can be calculated using the formula:
# F(n) = F(n-1) + F(n-2)

def fibonacci_recursive(n):
     """Return the nth Fibonacci number using recursion."""
     if n <= 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the function
print(fibonacci_recursive(10))  # Output: 55
print(fibonacci_recursive(0))   # Output: 0
print(fibonacci_recursive(1))   # Output: 1
print(fibonacci_recursive(2))   # Output: 1
print(fibonacci_recursive(3))   # Output: 2
print(fibonacci_recursive(4))   # Output: 3
print(fibonacci_recursive(5))   # Output: 5
print(fibonacci_recursive(6))   # Output: 8
print(fibonacci_recursive(7))   # Output: 13
print(fibonacci_recursive(8))   # Output: 21
print(fibonacci_recursive(9))   # Output: 34
print(fibonacci_recursive(10))  # Output: 55