# 📘 Program 31: Cube Sum of First N Natural Numbers (Python)

This Python program calculates the **sum of cubes** of the first **n natural numbers**.

---

## 📌 Problem Statement

**Write a Python program to find the cube sum of the first `n` natural numbers.**

---

## 🔢 What Are Natural Numbers?

Natural numbers are a set of **positive integers** starting from **1** and continuing indefinitely.

\[
\mathbb{N} = 1, 2, 3, 4, 5, \dots
\]

---

## 🧮 Formula for Cube Sum

The cube of a number is that number raised to the power of 3:

\[
\text{Cube of } n = n^3
\]

The **sum of cubes** of the first `n` natural numbers is given by the formula:

\[
1^3 + 2^3 + 3^3 + \dots + n^3 = \left(\frac{n(n + 1)}{2}\right)^2
\]

---

## ✅ Sample Code

```python
# Python program to find the cube sum of first n natural numbers

# Input from user
n = int(input("Enter the value of n: "))

# Using formula
cube_sum = ((n * (n + 1)) // 2) ** 2

# Display result
print(f"The sum of cubes of the first {n} natural numbers is: {cube_sum}")
```

---

## ▶️ Example Output

```bash
Enter the value of n: 5
The sum of cubes of the first 5 natural numbers is: 225
```

### 🧠 Explanation

\[
1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 1 + 8 + 27 + 64 + 125 = 225
\]

---

## 📁 Suggested Project Structure

```
cube_sum/
├── cube_sum.py
└── README.md
```

---

## 💡 Try This

- Calculate cube sum **using a loop** instead of formula.
- Ask the user to input **multiple numbers** and compute their cube sums.
- Visualize the cube values using a bar chart (`matplotlib`).

---
