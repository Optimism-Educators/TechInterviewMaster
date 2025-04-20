
# 🟩 Program 98: Check if Inequality Expression is Correct

This Python program checks whether a given inequality expression is correct. It returns `True` if the expression is valid, and `False` otherwise.

---

## 📌 Problem Statement

Create a function that checks if a given inequality expression is correct. The input is a string with comparison operators like `<` and `>`, and the program should evaluate whether the inequality holds true.

### Examples:

- For the input `"3 < 7 < 11"`, the function should return `True` because the inequality holds (`3 < 7` and `7 < 11`).
- For the input `"13 > 44 > 33 < 1"`, the function should return `False` because `13 > 44` is false.
- For the input `"1 < 2 < 6 < 9 > 3"`, the function should return `True` because the inequality holds.

---

## 🧠 Concepts Used

- String manipulation and splitting
- Evaluating inequalities using Python's built-in `eval()` function.

---

## 🧪 Sample Code

```python
def correct_signs(expression):
    return eval(expression)

# Test cases
print(correct_signs("3 < 7 < 11"))        # Output: True
print(correct_signs("13 > 44 > 33 < 1"))  # Output: False
print(correct_signs("1 < 2 < 6 < 9 > 3")) # Output: True
```

---

## 🎯 Example Input & Output

### Input

```
"3 < 7 < 11"
"13 > 44 > 33 < 1"
"1 < 2 < 6 < 9 > 3"
```

### Output

```
True
False
True
```

---

## ✅ Notes

- The function utilizes Python’s `eval()` to evaluate the inequality expression.
- The input is assumed to be a valid mathematical string containing comparison operators like `<` and `>`.
- Be cautious when using `eval()` in a real-world application, as it can execute arbitrary code and pose a security risk.

