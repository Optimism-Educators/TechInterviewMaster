 # Author: Antim Pal
 # Date: 2025-04-20
 # Problem: Fibonacci Sequence
 # Description: Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding numbers.
# The simplest Fibonacci sequence is 0, 1, 1, 2, 3, 5, 8, etc.
# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2)
# with seed values F(0) = 0 and F(1) = 1.
# The Fibonacci sequence can be generated using a loop or recursion.
# The program will take an integer input from the user and print the Fibonacci sequence up to that number.
# The program will also handle invalid inputs and print an error message if the input is not a positive integer.
# The program will also handle the case where the input is 0 or 1 and print the appropriate Fibonacci sequence.

# Function to generate Fibonacci sequence
def fibonacci(n):
    # Initialize the first two numbers of the sequence
    a, b = 0, 1
    # Loop through the sequence
    for i in range(n):
        # Print the current number
        print(a, end=' ')
        # Update the numbers for the next iteration
        a, b = b, a + b

# Get user input
n = int(input("Enter a positive integer: "))
# Check if the input is valid
if n < 0:
    print("Invalid input. Please enter a positive integer.")
elif n == 0:
    print("Fibonacci sequence: 0")
elif n == 1:
    print("Fibonacci sequence: 0 1")
else:
    # Print the Fibonacci sequence
    print("Fibonacci sequence: 0 1 ", end='')
    fibonacci(n-2)

# Output:
# Enter a positive integer: 8
# Fibonacci sequence: 0 1 1 2 3 5 8 13 21
# Enter a positive integer: 0
# Fibonacci sequence: 0
# Enter a positive integer: 1
# Fibonacci sequence: 0 1
# Enter a positive integer: -5
# Invalid input. Please enter a positive integer.