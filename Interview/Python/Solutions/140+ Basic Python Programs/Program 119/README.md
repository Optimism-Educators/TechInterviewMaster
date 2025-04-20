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
=======

## 📘 Program 119 – Alphabetical Order of Letters

### 📝 Description  

This program defines a function `alphabet_soup(s)` that takes a string as input and returns the string with its letters sorted in alphabetical order. The function sorts the characters in ascending order and returns the rearranged string.

---

### ✅ Examples

```python
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"
```

---

### 💡 Function Logic

- Convert the input string into a list of characters.
- Sort the list in alphabetical order.
- Join the sorted list of characters back into a string.
- Return the sorted string.

---

### 🧠 Function Definition

```python
def alphabet_soup(s):
    return ''.join(sorted(s))
```

---

### 🔁 How to Use

1. Provide a string of letters to the `alphabet_soup()` function.
2. The function sorts the characters of the string in alphabetical order.
3. The function returns the sorted string.
