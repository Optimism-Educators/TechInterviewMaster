# Program100
Here’s **Program 100** written in the format you requested:

---

```markdown
# 🟩 Program 100: Calculate Factorial Recursively

This Python program calculates the factorial of a number using recursion.

---

## 📌 Problem Statement

Write a function that calculates the factorial of a given number `n` recursively. The factorial of a non-negative integer `n` is the product of all positive integers less than or equal to `n`.

### Examples:

- For the input `factorial(5)`, the function should return `120`.
- For the input `factorial(3)`, the function should return `6`.
- For the input `factorial(1)`, the function should return `1`.
- For the input `factorial(0)`, the function should return `1`.

---

## 🧠 Concepts Used

- Recursion: The function calls itself with decreasing values until the base case is met.
- Factorial calculation.

---

## 🧪 Sample Code

```python
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Test cases
print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(1))  # Output: 1
print(factorial(0))  # Output: 1
```

---

## 🎯 Example Input & Output

### Input

```
factorial(5)
factorial(3)
factorial(1)
factorial(0)
```

### Output

```
120
6
1
1
```

---

## ✅ Notes

- The factorial of a number `n` is calculated as the product of all integers from `1` to `n`.
- The base case for recursion is when `n` is `0` or `1`, where the factorial is defined as `1`.
- This function uses a simple recursive approach to calculate the factorial.

---

Let me know if you need further adjustments! ✨

```
