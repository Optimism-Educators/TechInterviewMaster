# Program28
Certainly! Here's a complete and structured explanation for **Program 28 – Finding Factorial of a Number Using Recursion in Python**:

---

```markdown
# 🔢 Program 28: Factorial of a Number Using Recursion (Python)

This Python program calculates the **factorial** of a number using **recursion**.

---

## 📌 Problem Statement

**Write a Python program to find the factorial of a number using recursion.**

---

## 🧠 What is Factorial?

The **factorial** of a non-negative integer `n` is the product of all positive integers less than or equal to `n`. It is denoted as `n!`.

### 🧮 Factorial Definition:
\[
n! = n \times (n-1) \times (n-2) \times \dots \times 1
\]

For example:
- \( 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \)
- \( 0! = 1 \) (By definition)

---

## 🔄 How Does Recursion Work Here?

Recursion solves a problem by reducing it to smaller instances of the same problem. In this case, the factorial can be calculated recursively by multiplying `n` with the factorial of `n-1`.

### Recursive Formula:
\[
n! = n \times (n-1)!
\]
With the base case:
\[
0! = 1
\]

---

## ✅ Sample Code

```python
# Recursive function to find factorial
def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
num = int(input("Enter a number: "))

# Calculate and print factorial
print(f"The factorial of {num} is: {factorial(num)}")
```

---

## ▶️ Example Output

```bash
Enter a number: 5
The factorial of 5 is: 120
```

---

## 🧪 Important Notes on Recursion

- **Base Case**: In recursion, we need to define a base case to prevent infinite recursion. Here, the base case is `0! = 1`.
- **Recursive Case**: We multiply `n` with the factorial of `n-1` until we reach the base case.
- **Efficiency**: Recursive approaches can be less efficient for large numbers due to repeated calculations. Try using **memoization** to optimize.

---

## 📁 Suggested Project Structure

```
factorial_recursive/
├── factorial_recursive.py
└── README.md
```

---

## 💡 Bonus Ideas

- Add **input validation** (negative numbers, non-integer input).
- Explore **iterative** methods for computing factorial (for performance).
- Implement **memoization** to store previously computed factorials.

---
