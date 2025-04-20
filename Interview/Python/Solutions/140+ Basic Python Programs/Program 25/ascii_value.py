# Author: <Antim Pal>
# Date: <21-04-2025>
# Program: ASCII Value of a Character
# Description: Write a Python program to find the ASCII value of a character.
# Input: A single character
# Output: The ASCII value of the character

# Get input from the user
char = input("Enter a character: ")
# Check if the input is a single character
if len(char) == 1:
    # Get the ASCII value using the ord() function
    ascii_value = ord(char)
    # Print the ASCII value
    print(f"The ASCII value of '{char}' is {ascii_value}.")
else:
    print("Please enter a single character.")
# Example usage:
# Enter a character: A
# The ASCII value of 'A' is 65.
# Enter a character: a
# The ASCII value of 'a' is 97.   
# Enter a character: 1
# The ASCII value of '1' is 49.

# Enter a character: @
# The ASCII value of '@' is 64.
# Enter a character: !
# The ASCII value of '!' is 33.
# Enter a character: #
# The ASCII value of '#' is 35.
