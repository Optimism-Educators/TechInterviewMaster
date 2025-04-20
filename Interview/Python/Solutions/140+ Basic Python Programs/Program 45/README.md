
# 📝 Program 45: Check if the Given Number is a Happy Number (Python)

This Python program checks whether a given number is a **Happy Number**. A **Happy Number** is a number that, when you repeatedly replace it with the sum of the squares of its digits, eventually reaches 1. If it never reaches 1 and instead loops endlessly, the number is not a Happy Number.

---

## 📌 Problem Statement

**Write a Python program to check if the given number is a Happy Number.**

---

## 🔢 What is a Happy Number?

A **Happy Number** is defined as:
1. Start with a positive integer.
2. Replace the number with the sum of the squares of its digits.
3. Repeat the process until:
   - The number becomes 1 (the number is a Happy Number), or
   - The number falls into a cycle that does not include 1 (the number is not a Happy Number).

For example:
- **19** is a Happy Number because:
  \[
  1^2 + 9^2 = 82 \\
  8^2 + 2^2 = 68 \\
  6^2 + 8^2 = 100 \\
  1^2 + 0^2 + 0^2 = 1
  \]
  The number eventually becomes 1, so 19 is a Happy Number.

---

## ✅ Sample Code

```python
# Function to calculate the sum of squares of digits of a number
def sum_of_squares(num):
    return sum(int(digit) ** 2 for digit in str(num))

# Function to check if a number is a Happy Number
def is_happy_number(num):
    seen = set()  # To track numbers we have already seen (to detect cycles)
    
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum_of_squares(num)
    
    return num == 1

# Input from the user
num = int(input("Enter a number: "))

# Check and display if the number is a Happy Number
if is_happy_number(num):
    print(f"{num} is a Happy Number!")
else:
    print(f"{num} is not a Happy Number.")
```

---

## ▶️ Example Output

```bash
Enter a number: 19
19 is a Happy Number!
```

---

## 📁 Suggested Project Structure

```
happy_number/
├── happy_number.py
└── README.md
```

---

## 💡 You Can Try

- Check for **multiple numbers** in a range to find all Happy Numbers.
- Modify the program to **visualize the process** of summing the squares of digits.
- Extend the program to handle **negative numbers** and other edge cases.

---
 