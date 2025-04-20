# Program46
Here's the explanation and code for **Program 46: Print All Happy Numbers Between 1 and 100**:

---

```markdown
# 📝 Program 46: Print All Happy Numbers Between 1 and 100 (Python)

This Python program prints all **Happy Numbers** between 1 and 100. A **Happy Number** is a number that, when you repeatedly replace it with the sum of the squares of its digits, eventually reaches 1. If it never reaches 1 and instead loops endlessly, the number is not a Happy Number.

---

## 📌 Problem Statement

**Write a Python program to print all Happy Numbers between 1 and 100.**

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

# Function to print all Happy Numbers between 1 and 100
def print_happy_numbers(start, end):
    print(f"Happy Numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_happy_number(num):
            print(num, end=" ")

# Calling the function to print all Happy Numbers between 1 and 100
print_happy_numbers(1, 100)
```

---

## ▶️ Example Output

```bash
Happy Numbers between 1 and 100:
1 7 10 13 19 23 28 31 44 49 68 70 71 79 82 86 91 94 100
```

---

## 📁 Suggested Project Structure

```
happy_numbers/
├── happy_numbers.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to print Happy Numbers in **other ranges**, such as 101 to 200.
- Explore **Happy Numbers in different number systems** (e.g., binary, hexadecimal).
- Visualize the process of calculating the sum of the squares of digits for each number.

---
