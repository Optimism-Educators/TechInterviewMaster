# Program27
Certainly! Here's a complete and structured explanation for **Program 27 – Displaying Fibonacci Sequence Using Recursion in Python**, just like you asked:

---

```markdown
# 🌀 Program 27: Fibonacci Sequence Using Recursion (Python)

This Python program uses **recursion** to print the Fibonacci sequence up to a certain number of terms, as entered by the user.

---

## 📌 Problem Statement

**Write a Python program to display the Fibonacci sequence using recursion.**

---

## 🔢 What is the Fibonacci Sequence?

The **Fibonacci sequence** is a series of numbers where each number is the **sum of the two preceding ones**, usually starting with **0 and 1**.

### 🔁 Sequence Example:
```

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

```

### 🧮 Mathematical Recurrence Relation:

\[
F(0) = 0,\quad F(1) = 1,\quad F(n) = F(n-1) + F(n-2) \quad \text{for } n > 1
\]

---

## 🧠 Why Use Recursion?

Recursion simplifies problems by solving smaller instances of the same problem. In the case of Fibonacci, the same pattern is repeated.

---

## ✅ Sample Code

```python
# Recursive function to return Fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get user input for number of terms
terms = int(input("How many terms? "))

print(f"Fibonacci sequence using recursion (first {terms} terms):")
for i in range(terms):
    print(fibonacci(i), end=" ")
```

---

## ▶️ Example Output

```bash
How many terms? 8
Fibonacci sequence using recursion (first 8 terms):
0 1 1 2 3 5 8 13
```

---

## 🧪 Note on Performance

- **Recursive Fibonacci** has exponential time complexity (**O(2^n)**).
- For large `n`, it becomes **inefficient** due to repeated calculations.

✅ Try **Memoization** or **Dynamic Programming** for better performance!

---

## 📁 Suggested Project Structure

```
fibonacci_recursive/
├── fibonacci_recursive.py
└── README.md
```

---

## 💡 Bonus Ideas

- Add **input validation** (negative numbers, non-integers).
- Visualize the recursive call tree with graphs.
- Convert the recursion into **tail recursion** or use **iterative version** for efficiency.

---

