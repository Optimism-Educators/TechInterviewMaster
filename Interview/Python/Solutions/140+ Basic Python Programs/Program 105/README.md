
# 📘 Program 105: Recursive Factorial Function

## 🧮 Description

This Python program defines a **recursive function** to compute the factorial of a non-negative integer.  
The factorial of a number `n` is defined as:

```

n! = n × (n - 1) × (n - 2) × ... × 1  
0! = 1

```

This program uses recursion to solve the problem efficiently.

---

## 📌 Function Definition

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

---

## ✅ Examples

```python
print(factorial(5))  # ➞ 120
print(factorial(3))  # ➞ 6
print(factorial(1))  # ➞ 1
print(factorial(0))  # ➞ 1
```

### 💡 Output

```
120
6
1
1
```

---

## 📂 Use Cases

- Mathematical computations
- Combinatorics (e.g., calculating permutations and combinations)
- Recursion practice for beginners

---

## 🛡️ Notes

- Input should be a non-negative integer.
- Recursive approach can hit a recursion depth limit for very large numbers.

