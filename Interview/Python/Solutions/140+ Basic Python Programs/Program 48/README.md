# Program48
Here's the explanation and code for **Program 48: Print all Pronic Numbers Between 1 and 100**:

---

```markdown
# 📝 Program 48: Print All Pronic Numbers Between 1 and 100 (Python)

This Python program prints all **pronic numbers** (also known as oblong or rectangular numbers) between 1 and 100. A pronic number is the product of two consecutive integers, \(n\) and \(n + 1\). Mathematically, a pronic number is expressed as:

\[
P_n = n \times (n + 1)
\]

---

## 📌 Problem Statement

**Write a Python program to print all pronic numbers between 1 and 100.**

---

## 🔢 What is a Pronic Number?

A **pronic number** is the product of two consecutive integers. The first few pronic numbers are:
- \( P_1 = 1 \times (1 + 1) = 2 \)
- \( P_2 = 2 \times (2 + 1) = 6 \)
- \( P_3 = 3 \times (3 + 1) = 12 \)
- \( P_4 = 4 \times (4 + 1) = 20 \)

Pronic numbers can be used to represent areas of rectangular shapes with integer side lengths. The sequence starts with 2 and continues as \( 6, 12, 20, 30, 42, 56, \dots \).

---

## ✅ Sample Code

```python
# Function to find pronic numbers up to 100
def print_pronic_numbers(limit):
    pronic_numbers = []
    n = 1
    while True:
        pronic = n * (n + 1)
        if pronic > limit:
            break
        pronic_numbers.append(pronic)
        n += 1
    return pronic_numbers

# Set the upper limit
limit = 100

# Get and print all pronic numbers between 1 and 100
pronic_numbers = print_pronic_numbers(limit)
print(f"Pronic numbers between 1 and {limit}: {pronic_numbers}")
```

---

## ▶️ Example Output

```bash
Pronic numbers between 1 and 100: [2, 6, 12, 20, 30, 42, 56, 72, 90]
```

---

## 📁 Suggested Project Structure

```
pronic_numbers/
├── pronic_numbers.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to **print pronic numbers in a different range**, like 1 to 500 or 1 to 1000.
- Explore **pronic numbers in other contexts**, such as geometric or combinatorial problems.
- Implement the program to **identify pronic numbers** for any given upper limit from user input.

---
