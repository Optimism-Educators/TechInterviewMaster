# Program 21: Find the Sum of Natural Numbers

## 🧮 Problem Statement

Write a Python program to **find the sum of natural numbers** up to a given number `n`.

---

## 🔍 What Are Natural Numbers?

Natural numbers are a set of positive integers that are used to **count and order objects**.  
They start from **1** and go on infinitely:

\[
\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, 8, \ldots\}
\]

---

## 🧠 Concept

To find the sum of the first `n` natural numbers, we can use:
- **Loop-based approach** – Iteratively add numbers from 1 to `n`
- **Formula-based approach** – Use the formula:

\[
\text{Sum} = \frac{n(n+1)}{2}
\]

---

## 🧑‍💻 Python Code (Using Loop)

```python
# Python program to find the sum of natural numbers

# Input from user
num = int(input("Enter a positive number: "))

# Check if the number is positive
if num < 1:
    print("Please enter a number greater than 0.")
else:
    total = 0
    for i in range(1, num + 1):
        total += i
    print(f"The sum of the first {num} natural numbers is {total}")
```

---

## 🧑‍💻 Python Code (Using Formula)

```python
# Python program to find the sum using formula

# Input from user
num = int(input("Enter a positive number: "))

if num < 1:
    print("Please enter a number greater than 0.")
else:
    total = num * (num + 1) // 2
    print(f"The sum of the first {num} natural numbers is {total}")
```

---

## ✅ Sample Output

```
Enter a positive number: 5
The sum of the first 5 natural numbers is 15
```

---

## 🧠 Tip

Using the formula is faster and more efficient, especially for large values of `n`.

---

## 📘 Related Topics

- Loops in Python
- Arithmetic Progressions
- Mathematical formulae in programming

---
