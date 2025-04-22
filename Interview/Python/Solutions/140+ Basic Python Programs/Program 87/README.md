
# 🔢 Program 87: Generator to Print Numbers Divisible by 5 and 7

This Python program uses a **generator** to print all numbers between **0 and n** that are divisible by both **5 and 7** (i.e., divisible by 35), in **comma-separated** format.

---

## 📌 Problem Statement

Write a Python program using a **generator** to print numbers which are divisible by **5 and 7** between **0 and n** (inclusive).  
The value of `n` should be accepted from the user as input.

---

## 🧠 Concepts Used

- Generator function
- Modulus operator
- List comprehension and string joining

---

## 🧪 Sample Code

```python
def divisible_by_5_and_7(n):
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

# Input from user
n = int(input("Enter the value of n: "))

# Using generator and printing comma-separated output
result = [str(num) for num in divisible_by_5_and_7(n)]
print(",".join(result))
```

---

## 🎯 Example Input & Output

### Input

```
Enter the value of n: 100
```

### Output

```
0,35,70
```

---

## ✅ Notes

- The generator improves memory efficiency especially for large values of `n`.
- `yield` is used to produce values one by one, making the function more efficient.

---
