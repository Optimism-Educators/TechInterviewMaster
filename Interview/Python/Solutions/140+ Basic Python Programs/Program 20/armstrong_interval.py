# Author: Antim Pal
# Date: 2025-04-21
# Description: This program finds all Armstrong numbers in a given interval.
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.    
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
# The program takes two integers as input, representing the start and end of the interval.
# It then iterates through each number in the interval, checks if it is an Armstrong number, and prints the result.
# The program uses a helper function `is_armstrong` to check if a number is an Armstrong number.
# The function converts the number to a string to easily access its digits and calculate the sum of the digits raised to the power of the number of digits.
# The program handles invalid input by checking if the start of the interval is less than or equal to the end.
# If the interval is invalid, the program prints an error message.
# Armstrong numbers are also known as narcissistic numbers or pluperfect digital invariants.`

def is_armstong(num):
     """
     Check if a number is an Armstrong number.
     
     An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
     
     Args:
     num (int): The number to check.
     
     Returns:
     bool: True if the number is an Armstrong number, False otherwise.
     """
     num_str = str(num)  # Convert the number to a string to access its digits
     num_digits = len(num_str)  # Get the number of digits in the number
     sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)  # Calculate the sum of the digits raised to the power of the number of digits
     return sum_of_digits == num

start = int(input("Enter the start of the interval: "))  # Get the start of the interval from the user
end = int(input("Enter the end of the interval: "))  # Get the end of the interval from the user

if start <= end:
     print("Armstrong number in the interval:")  # Check if the start of the interval is less than or equal to the end
     for num in range(start, end + 1):  # Iterate through the numbers in the interval
          if is_armstrong(num):  # Check if the number is an Armstrong number
               print(num) # Print the Armstrong number
else:
     print("Invalid interval. Start should be less than or equal to end.")  # Print an error message if the interval is invalid  
# The program takes two integers as input, representing the start and end of the interval.


"""
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_digits == num

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

if start <= end:
    print("Armstrong numbers in the interval:")
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num)
else:
    print("Invalid interval. Start should be less than or equal to end.")
# This program finds all Armstrong numbers in a given interval.
"""
    
# The program uses a simple loop to iterate through the numbers in the interval and checks each number using the `is_armstrong` function.
# If a number is found to be an Armstrong number, it is printed to the console.
# The program handles invalid input by checking if the start of the interval is less than or equal to the end.
# If the interval is invalid, the program prints an error message.