# Program119

# `count_vowels` Function

## Description

The `count_vowels` function takes a string as input and returns the number of vowels (`a`, `e`, `i`, `o`, `u`) present in the string.  
It is **case-insensitive**, meaning it treats uppercase and lowercase letters the same.

## Usage

```python
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
```

# Parameters
s (str): The input string to analyze.

# Returns
int: The number of vowels found in the input string.

Example

```python
print(count_vowels("Hello, World!"))  # Output: 3
print(count_vowels("Python"))         # Output: 1
print(count_vowels("AEIOU"))          # Output: 5
```

Notes
The function does not count y as a vowel.

It ignores any non-alphabetical characters.

It works with any string, including empty ones.
