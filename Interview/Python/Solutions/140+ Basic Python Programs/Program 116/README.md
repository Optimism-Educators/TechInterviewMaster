# Program116
Here's a **README.md** file for **Program 116 – Missing Number Finder**:

---

## 📘 Program 116 – Missing Number Finder

### 📝 Description

This Python program defines a function `missing_num()` that takes a list of 9 integers between 1 and 10 (inclusive), where exactly one number is missing. The function returns the missing number.

It uses the mathematical fact that the sum of the first 10 natural numbers is **55**. By subtracting the sum of the given list from 55, the missing number is found.

---

### ✅ Examples

```python
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10
missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7
```

---

### 💡 Logic

- Sum of numbers from 1 to 10: `1 + 2 + ... + 10 = 55`
- Subtract the sum of the input list from 55 to find the missing number.

---

### 🧠 Function Definition

```python
def missing_num(lst):
    return 55 - sum(lst)
```

---

### 🔁 How to Use

1. Define a list of 9 unique integers from 1 to 10.
2. Call the `missing_num()` function with the list as an argument.
3. Get the missing number as the output.

---

Let me know if you'd like this exported to a `.md` file or added to a GitHub repo layout!
