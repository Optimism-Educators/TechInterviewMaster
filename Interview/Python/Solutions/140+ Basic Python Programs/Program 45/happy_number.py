# Author: <Antim Pal>
# Date: <22-04-2025>
# Discription: Write a program to check if a number is a happy number or not. A happy number is a number which leads to 1 after repeatedly replacing it with the sum of the square of its digits. For example, 19 is a happy number: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1. If a number is not a happy number, the process will be stuck in a cycle that does not include 1.

# This program checks if a number is a happy number or not.
# A happy number is a number which leads to 1 after repeatedly replacing it with the sum of the square of its digits.
# For example, 19 is a happy number: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.
# If a number is not a happy number, the process will be stuck in a cycle that does not include 1.

# Function to check if a number is a happy number
def is_happy_number(num):
    # Use a set to track numbers we have already seen to detect cycles
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)  # Add the current number to the set
        # Replace the number with the sum of the squares of its digits
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1  # Return True if the number is 1, otherwise False

# Example usage
# Check if the number 19 is a happy number
number = int(input("Enter a number: "))  # Get the number from the user
if is_happy_number(number):
    print(f"{number} is a happy number.")
else:
    print(f"{number} is not a happy number.")
