# Program65
Here is **Program 65** in the requested format:

---

```markdown
# 📝 Program 65: Find All Duplicate Characters in a String (Python)

This Python program identifies all the **duplicate characters** in a given string.

---

## 📌 Problem Statement

**Write a Python program to find all duplicate characters in a string.**

---

## 💡 What are Duplicate Characters?

**Duplicate characters** are those characters that appear more than once in the string. The program should identify and list these characters.

For example:
- String: `"programming"`

The **duplicate characters** would be: `"r", "g", "m"`

---

## ✅ Sample Code

```python
# Function to find duplicate characters in a string
def find_duplicates(string):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # List characters that occur more than once
    duplicates = [char for char, count in char_count.items() if count > 1]

    return duplicates

# Input string from user
input_string = input("Enter a string: ")

# Find and display duplicate characters
duplicates = find_duplicates(input_string)
print("Duplicate characters:", duplicates)
```

---

## ▶️ Example Output

```bash
Enter a string: programming
Duplicate characters: ['r', 'g', 'm']
```

---

## 🔍 Explanation

1. **Counting occurrences**: We iterate through the string and count the occurrences of each character using a dictionary.
2. **Finding duplicates**: The list comprehension checks for characters that appear more than once and stores them in the `duplicates` list.

---

📘 This program is useful for detecting repeated characters in strings and can be applied in text analysis or string manipulation tasks.

```

---

Let me know if you'd like another program or more clarification! 😊
