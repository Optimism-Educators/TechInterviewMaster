
# 📝 Program 62: Split and Join a String (Python)

This Python program demonstrates how to **split a string into a list of words** and then **join them back** into a single string using a different separator.

---

## 📌 Problem Statement

**Write a Python program to split a string into words and join them back using a specified separator.**

---

## 💡 Understanding the Concepts

- **Splitting a string**: Converts the string into a list of words using `.split()` (default delimiter is space).
- **Joining a list**: Combines a list of words back into a string using `'separator'.join(list)`.

---

## ✅ Sample Code

```python
# Input string
input_str = input("Enter a string: ")

# Split the string into a list of words
words = input_str.split()

# Join the list back into a string using a hyphen (-) as separator
joined_str = '-'.join(words)

# Output
print("List after splitting:", words)
print("String after joining with '-':", joined_str)
```

---

## ▶️ Example Output

```bash
Enter a string: Python is awesome
List after splitting: ['Python', 'is', 'awesome']
String after joining with '-': Python-is-awesome
```

---

## ⚠️ Notes

- You can use other separators like commas `,`, underscores `_`, or any custom character.
- Very useful in formatting strings, processing user input, and preparing data for display or export.

---
