
## 📘 Program 137 – Count Equal Integers

### 📝 Description  
This program defines a function `equal()` that takes three integer arguments and returns the number of integers that are of equal value. The function checks if any two or three integers are the same and returns the appropriate count: `0`, `2`, or `3`. If all the integers are the same, it returns `3`, if two integers are the same, it returns `2`, and if no integers are the same, it returns `0`.

### ✅ Examples

```python
equal(3, 4, 3)
# ➞ 2
# The integers 3 and 3 are equal.

equal(1, 1, 1)
# ➞ 3
# All three integers are equal.

equal(3, 4, 1)
# ➞ 0
# No integers are equal.
```

---

### 🧠 Function Logic

- **equal(a, b, c)**:
  - The function takes three integers as input.
  - It compares the three integers to determine if any of them are equal.
  - If two integers are equal, the function returns `2`.
  - If all three integers are equal, it returns `3`.
  - If none of the integers are equal, the function returns `0`.

---

### 🧠 Function Definition

```python
def equal(a, b, c):
    # Check how many integers are equal
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0
```

---

### 🔁 How to Use

1. Pass three integers to the `equal()` function.
2. The function will check how many of the integers are equal and return either `0`, `2`, or `3`.

### 💡 Example Usage

```python
# Input integers
a = 3
b = 4
c = 3

# Call the function
result = equal(a, b, c)

# Output the result
print(result)  # Output: 2
```

---

### 🧠 Example Walkthrough

For the input `(3, 4, 3)`:
- The integers 3 and 3 are equal, so the function will return `2`.

For the input `(1, 1, 1)`:
- All three integers are equal, so the function will return `3`.

For the input `(3, 4, 1)`:
- No integers are equal, so the function will return `0`.

---

### 🧠 Additional Notes

- The function only compares the three integers to check for equality.
- The function is designed to return `0`, `2`, or `3` based on the number of equal integers.

---

### 🔍 Example Input/Output

- **Input**: `(3, 4, 3)`
  - **Output**: `2`

- **Input**: `(1, 1, 1)`
  - **Output**: `3`

- **Input**: `(3, 4, 1)`
  - **Output**: `0`
