# Program94
Here’s **Program 94** written in the format you requested:

---

```markdown
# 🟩 Program 94: Curzon Number Check

This Python program defines a function `is_curzon()` that checks whether a given integer is a **Curzon number**.

---

## 📌 Problem Statement

A number is a **Curzon number** if it satisfies the following condition:

\[
\frac{2^n + 1}{2n + 1}
\]

If \( 2^n + 1 \) is divisible by \( 2n + 1 \), then the number \( n \) is a Curzon number.

### Example:

For `n = 5`:
- \( 2^5 + 1 = 33 \)
- \( 2 \times 5 + 1 = 11 \)
- \( 33 \) is divisible by \( 11 \), so `5` is a Curzon number.

For `n = 10`:
- \( 2^{10} + 1 = 1025 \)
- \( 2 \times 10 + 1 = 21 \)
- \( 1025 \) is not divisible by \( 21 \), so `10` is not a Curzon number.

---

## 🧠 Concepts Used

- Mathematical Calculations
- Divisibility Check
- Power Function

---

## 🧪 Sample Code

```python
def is_curzon(num):
    # Check if (2^num + 1) is divisible by (2 * num + 1)
    return (2 ** num + 1) % (2 * num + 1) == 0

# Test cases
print(is_curzon(5))  # Output: True
print(is_curzon(10)) # Output: False
print(is_curzon(14)) # Output: True
```

---

## 🎯 Example Input & Output

### Input

```
5
10
14
```

### Output

```
True
False
True
```

---

## ✅ Notes

- The function uses the `**` operator to calculate the power of 2 raised to the given number.
- It checks the divisibility condition using the modulo `%` operator.
- The result is `True` if the number is a Curzon number, and `False` otherwise.

---
