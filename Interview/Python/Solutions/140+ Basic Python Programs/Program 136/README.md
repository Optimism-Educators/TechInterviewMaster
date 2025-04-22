
## 📘 Program 136 – Validate Pythagorean Triplet

### 📝 Description  

This program defines a function `is_triplet()` that validates whether three given integers form a Pythagorean triplet. A Pythagorean triplet consists of three integers where the sum of the squares of the two smallest integers equals the square of the largest integer. The function checks if this condition is met and returns `True` or `False`.

### ✅ Examples

```python
is_triplet(3, 4, 5)
# ➞ True
# 3² + 4² = 25, 5² = 25

is_triplet(13, 5, 12)
# ➞ True
# 5² + 12² = 169, 13² = 169

is_triplet(1, 2, 3)
# ➞ False
# 1² + 2² = 5, 3² = 9
```

---

### 🧠 Function Logic

- **is_triplet(a, b, c)**:
  - The function takes three integers as inputs.
  - It first sorts the integers to identify the smallest, middle, and largest numbers.
  - The function checks whether the sum of the squares of the two smallest numbers is equal to the square of the largest number.
  - If the condition holds true, the function returns `True`. Otherwise, it returns `False`.

---

### 🧠 Function Definition

```python
def is_triplet(a, b, c):
    # Sort the numbers
    a, b, c = sorted([a, b, c])

    # Check the Pythagorean condition
    return a**2 + b**2 == c**2
```

---

### 🔁 How to Use

1. Pass three integers to the `is_triplet()` function.
2. The function will validate whether the integers form a Pythagorean triplet and return `True` or `False`.

### 💡 Example Usage

```python
# Input integers
a = 3
b = 4
c = 5

# Call the function
result = is_triplet(a, b, c)

# Output the result
print(result)  # Output: True
```

---

### 🧠 Example Walkthrough

For the input `(3, 4, 5)`:

- The two smallest numbers are 3 and 4, and the largest number is 5.
- The sum of squares of 3 and 4 is: `3² + 4² = 9 + 16 = 25`.
- The square of 5 is: `5² = 25`.
- Since the condition holds true, the result is `True`.

For the input `(13, 5, 12)`:

- The two smallest numbers are 5 and 12, and the largest number is 13.
- The sum of squares of 5 and 12 is: `5² + 12² = 25 + 144 = 169`.
- The square of 13 is: `13² = 169`.
- Since the condition holds true, the result is `True`.

For the input `(1, 2, 3)`:

- The two smallest numbers are 1 and 2, and the largest number is 3.
- The sum of squares of 1 and 2 is: `1² + 2² = 1 + 4 = 5`.
- The square of 3 is: `3² = 9`.
- Since the condition does not hold, the result is `False`.

---

### 🧠 Additional Notes

- The function first sorts the input numbers to ensure the largest number is compared with the sum of the squares of the smaller two numbers.
- The input numbers do not need to be sorted before passing them to the function.

---

### 🔍 Example Input/Output

- **Input**: `(3, 4, 5)`
  - **Output**: `True`

- **Input**: `(13, 5, 12)`
  - **Output**: `True`

- **Input**: `(1, 2, 3)`
  - **Output**: `False`
