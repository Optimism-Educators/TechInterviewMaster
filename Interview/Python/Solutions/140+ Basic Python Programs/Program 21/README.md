
# 📘 Program 21: Find the Sum of Natural Numbers

This Python program calculates the **sum of the first `n` natural numbers**, where `n` is a positive integer input by the user.

---

## 📌 Problem Statement

**Write a Python program to find the sum of natural numbers up to a given number `n`.**

---

## 🔍 What are Natural Numbers?

Natural numbers are **positive integers** that are used for counting.  
They are the basic numbers starting from **1** and go on indefinitely.

### ℕ = {1, 2, 3, 4, 5, 6, ...}

---

## 🧠 Concept

To calculate the sum of the first `n` natural numbers, we have two options:

### 1️⃣ Loop-based Approach:
Add numbers from 1 to `n` using a loop.

### 2️⃣ Formula-based Approach:
Use the formula:
\[
\text{Sum} = \frac{n(n + 1)}{2}
\]

---

## ✅ Python Code (Using Loop)

```python
# Python program to find the sum of natural numbers using a loop

# Take input from user
num = int(input("Enter a positive number: "))

if num < 1:
    print("Please enter a positive integer.")
else:
    total = 0
    for i in range(1, num + 1):
        total += i
    print(f"The sum of the first {num} natural numbers is {total}")
```

---

## ✅ Python Code (Using Formula)

```python
# Python program to find the sum of natural numbers using a formula

# Take input from user
num = int(input("Enter a positive number: "))

if num < 1:
    print("Please enter a positive integer.")
else:
    total = num * (num + 1) // 2
    print(f"The sum of the first {num} natural numbers is {total}")
```

---

## ▶️ Sample Output

```bash
Enter a positive number: 5
The sum of the first 5 natural numbers is 15
```

---

## 📁 Suggested Folder Structure

```
sum_natural_numbers/
├── sum_using_loop.py
├── sum_using_formula.py
└── README.md
```

---

## 💡 Try It Yourself

- What happens when `n = 1`?
- Can you write a function that takes any list of numbers and returns their sum?

---
