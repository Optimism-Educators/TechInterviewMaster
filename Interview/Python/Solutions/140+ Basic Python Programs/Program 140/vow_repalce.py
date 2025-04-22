# Replace all the vowels in a string with a specified character.
# Author: Antim Pal (antimpal.113@gmail.com)
# Date: 2025-04-20
# Description: This program replaces all the vowels in a given string with a specified character.
# The program takes a string and a character as input and returns the modified string with vowels replaced.
def replace_vowels(input_string, replacement_char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    modified_string = ""
    for char in input_string:
        if char.lower() in vowels:
            modified_string += replacement_char
        else:
            modified_string += char
    return modified_string

input_string = input("Enter a string: ")
replacement_char = input("Enter the character to replace vowels: ")
modified_string = replace_vowels(input_string, replacement_char)
print("Modified string:", modified_string)

# Example usage:
# Input: "Hello World", Replacement Character: "*"
# Output: "H*ll* W*rld"
# Explanation: The vowels in the input string "Hello World" are 'e', 'o', and 'o'. They are replaced with the specified character '*', resulting in "H*ll* W*rld".
