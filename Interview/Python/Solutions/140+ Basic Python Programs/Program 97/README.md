
# 🟩 Program 97: Sum of Numbers Divisible by `c` in a Range

This Python program calculates the sum of numbers in a given range that are evenly divisible by a specified number `c`.

---

## 📌 Problem Statement

The task is to create a function that takes three arguments: `a`, `b`, and `c`. The function should return the sum of all numbers within the range `[a, b]` that are divisible by `c`.

### Example:

For `a = 1`, `b = 10`, and `c = 20`:
- The result is `0` because no number between 1 and 10 can be evenly divided by 20.

For `a = 1`, `b = 10`, and `c = 2`:
- The result is `30` because `2 + 4 + 6 + 8 + 10 = 30`.

For `a = 1`, `b = 10`, and `c = 3`:
- The result is `18` because `3 + 6 + 9 = 18`.

---

## 🧠 Concepts Used

- Looping through a range of numbers
- Modulo operation to check divisibility

---

## 🧪 Sample Code

```python
def evenly_divisible(a, b, c):
    return sum(x for x in range(a, b + 1) if x % c == 0)

# Test cases
print(evenly_divisible(1, 10, 20))  # Output: 0
print(evenly_divisible(1, 10, 2))   # Output: 30
print(evenly_divisible(1, 10, 3))   # Output: 18
```

---

## 🎯 Example Input & Output

### Input

```
(1, 10, 20)
(1, 10, 2)
(1, 10, 3)
```

### Output

```
0
30
18
```

---

## ✅ Notes

- The function uses list comprehension with `sum()` to calculate the sum of the numbers that satisfy the divisibility condition (`x % c == 0`).
- The range function `range(a, b + 1)` includes both `a` and `b`, ensuring the full range is checked.

