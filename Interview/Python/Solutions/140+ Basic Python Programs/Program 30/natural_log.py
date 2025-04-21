# Author: <Antim Pal>
# Date: 21-04-2025
# Description: Program to calculate the natural logarithm of a number using Taylor series expansion.
# The Taylor series expansion for ln(1+x) is given by:
# ln(1+x) = x - (x^2)/2 + (x^3)/3 - (x^4)/4 + ... + ((-1)^(n-1) * x^n)/n
# where n is the number of terms in the series.   
# The series converges for -1 < x <= 1.
# The natural logarithm of a number x can be calculated using the formula:
# ln(x) = ln(1 + (x-1)) = ln(1 + y) where y = x - 1
# The series converges for -1 < y <= 1.
# The program takes a number as input and calculates its natural logarithm using the Taylor series expansion.
# The program also checks if the input number is valid (greater than 0) and handles invalid inputs gracefully.
# The program uses the math module to calculate the power of a number and the factorial of a number.
# The program also uses the time module to measure the execution time of the program.
# The program uses the time module to measure the execution time of the program.

import time

def natural_log(x, n_terms=1000):
     """
     Calculate the natural logarithm of a number using Taylor series expansion.
     
     Parameters:
     x (float): The number to calculate the natural logarithm for.
     n_terms (int): The number of terms in the Taylor series expansion.
     
     Returns:
     float: The natural logarithm of the number.
     """
     if x <= 0:
          raise ValueError("Input must be greater than 0.")
     
     # Calculate y = x - 1
     y = x - 1
     
     # Check if y is within the convergence range
     if y < -1 or y > 1:
          raise ValueError("The series converges for -1 < y <= 1.")
     
     ln_x = 0.0
     for n in range(1, n_terms + 1):
          term = ((-1) ** (n - 1)) * (y ** n) / n
          ln_x += term
     
     return ln_x

# Example usage
x = 2.718281828459045
n_terms = 1000
try:
    start_time = time.time()
    result = natural_log(x, n_terms)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The natural logarithm of {x} is approximately {result:.10f}")
    print(f"Execution time: {execution_time:.6f} seconds")
except ValueError as e:
    print(f"Error: {e}")
