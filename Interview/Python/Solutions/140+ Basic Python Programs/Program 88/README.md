
# 🔢 Program 88: Generator to Print Even Numbers Between 0 and n

This Python program uses a **generator** to print all **even numbers** between **0 and n** (inclusive), in **comma-separated** format.

---

## 📌 Problem Statement

Write a Python program using a **generator** to print **even numbers** between **0 and n** (inclusive).  
The value of `n` should be accepted from the user as input.

---

## 🧠 Concepts Used

- Generator functions
- Modulus operator `%`
- List comprehension
- `str.join()` for formatted output

---

## 🧪 Sample Code

```python
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Input from user
n = int(input("Enter the value of n: "))

# Using the generator to get even numbers
even_nums = [str(num) for num in even_numbers(n)]
print(",".join(even_nums))
```

---

## 🎯 Example Input & Output

### Input

```
Enter the value of n: 10
```

### Output

```
0,2,4,6,8,10
```

---

## ✅ Notes

- Even numbers are those which are divisible by 2 (`i % 2 == 0`).
- Generators help in producing one value at a time, which is memory efficient.

---
