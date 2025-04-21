# Author: <Antim Pal>
# Date: <21-04-2025
# Program Description: Sort the words in a sentence in alphabetical order using Python
# Input: Take a sentence as input from the user
# Process: Sort the words in a sentence in alphabetical order using Python
# Output: Print the sorted words in a sentence in alphabetical order using Python

# Take a sentence as input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Sort the words in alphabetical order
words.sort()

# Print the sorted words in a sentence in alphabetical order using Python
print("Sorted words in a sentence in alphabetical order using Python:")
for word in words:
    print(word)
    
# Output:
# Enter a sentence: Hello world
# Sorted words in a sentence in alphabetical order using Python:
# Hello
# world
# 
# Enter a sentence: Python is a programming language
# Sorted words in a sentence in alphabetical order using Python:
# is
# a
# language
# programming
# Python
# 
# Enter a sentence: This is a test sentence
# Sorted words in a sentence in alphabetical order using 