# Program63
Sure! Here's **Program 63** formatted just the way you like:

---

```markdown
# 📝 Program 63: Check if a Given String is a Binary String (Python)

This Python program checks whether a given string consists **only of binary digits (0 and 1)**.

---

## 📌 Problem Statement

**Write a Python program to check if a given string is a binary string.**

---

## 💡 What is a Binary String?

A **binary string** is a string that contains only the characters **'0'** and **'1'**.

For example:
- ✅ `"10101"` is a binary string.
- ❌ `"12301"` is not a binary string.

---

## ✅ Sample Code

```python
# Function to check if a string is binary
def is_binary_string(s):
    for char in s:
        if char not in ('0', '1'):
            return False
    return True

# Input from user
string = input("Enter a string: ")

# Check and display result
if is_binary_string(string):
    print(f'"{string}" is a binary string.')
else:
    print(f'"{string}" is NOT a binary string.')
```

---

## ▶️ Example Output

```bash
Enter a string: 101010
"101010" is a binary string.

Enter a string: 12345
"12345" is NOT a binary string.
```

---

## 🔍 Tip

You can also use Python sets for a more concise version:

```python
def is_binary_string(s):
    return set(s).issubset({'0', '1'})
```

---
