# 🔢 Program: Find the Least Common Multiple (LCM) in Python

This Python program calculates the **Least Common Multiple (LCM)** of two numbers entered by the user.

---

## 📌 Problem Statement

**Write a Python Program to Find the Least Common Multiple (LCM) of two numbers.**

---

## 🧠 What is LCM?

The **Least Common Multiple (LCM)** of two or more integers is the **smallest positive number** that is **evenly divisible** by each of the numbers.

For example:
- LCM of 4 and 5 is 20
- LCM of 6 and 8 is 24

---

## 🧮 LCM Formula

For two numbers `a` and `b`, the LCM is calculated using their **Greatest Common Divisor (GCD)**:

\[
\text{LCM}(a, b) = \frac{|a \times b|}{\text{GCD}(a, b)}
\]

📌 *GCD (Greatest Common Divisor)* is the largest positive integer that divides both `a` and `b` without leaving a remainder.

---

## ✅ Python Code

```python
import math

# Function to find LCM
def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

lcm = find_lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is {lcm}")
```

---

## ▶️ Sample Output

```
Enter first number: 12
Enter second number: 15
The LCM of 12 and 15 is 60
```

---

## 🔁 Extension: LCM of More Than Two Numbers

You can also compute LCM for multiple numbers step by step:

```python
from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

# Example usage:
nums = [4, 5, 10]
print(f"LCM of {nums} is {lcm_multiple(nums)}")
```

---

## 📁 Suggested File Structure

```
lcm_program/
├── lcm_two_numbers.py
├── lcm_multiple_numbers.py
└── README.md
```

---

## 💡 Challenge Yourself

- Write a version that takes input for a list of numbers.
- Create a GUI version using Tkinter.
- Visualize multiples using matplotlib.

