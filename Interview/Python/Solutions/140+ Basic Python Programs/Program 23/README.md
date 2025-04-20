Here’s a polished and structured `README.md` for **Program 23 – Find HCF (Highest Common Factor)** in Python:

---

```markdown
# 🧮 Program 23: Find HCF (Highest Common Factor) in Python

This program allows the user to calculate the **Highest Common Factor (HCF)** of two integers using a simple algorithm.

---

## 📌 Problem Statement

**Write a Python Program to Find HCF of two numbers.**

---

## 🧠 What is HCF?

The **Highest Common Factor (HCF)**, also known as the **Greatest Common Divisor (GCD)**, is the **largest positive integer** that **divides two or more numbers** without leaving a remainder.

### 📌 Example:
- HCF of 54 and 24 is **6**
- HCF of 15 and 25 is **5**

---

## 🧮 HCF Formula

You can use the built-in `math.gcd()` function or implement a loop-based method.

> \[
> \text{HCF}(a, b) = \text{GCD}(a, b)
> \]

For more than two numbers, HCF can be calculated step by step:
1. HCF of first two numbers.
2. Then HCF of the result with the next number.
3. Repeat until all numbers are processed.

---

## ✅ Python Code

### ▶️ Method 1: Using Euclidean Algorithm (Recommended)

```python
import math

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate HCF
hcf = math.gcd(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}")
```

---

### ▶️ Method 2: Custom Loop-Based Implementation

```python
# Function to compute HCF
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Result
print("The HCF is", compute_hcf(num1, num2))
```

---

## 💡 Sample Output

```bash
Enter first number: 54
Enter second number: 24
The HCF of 54 and 24 is 6
```

---

## 🗂️ Suggested File Structure

```
hcf_program/
├── hcf_builtin.py
├── hcf_custom.py
└── README.md
```

---

## 🔁 Extension Ideas

- Accept a list of numbers and compute their HCF.
- Create a GUI using Tkinter for user interaction.
- Combine with LCM logic to show both.

---

## 📚 Related Concepts

- **LCM (Least Common Multiple)**
- **Euclidean Algorithm**
- **Prime Factorization (alternative method for HCF)**

---
