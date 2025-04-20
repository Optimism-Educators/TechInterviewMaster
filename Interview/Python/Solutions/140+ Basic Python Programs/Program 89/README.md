
# 🔢 Program 89: Fibonacci Sequence Using List Comprehension

This Python program computes the **Fibonacci Sequence** based on the given input `n`, using **list comprehension** to generate and print the sequence in **comma-separated** form.

---

## 📌 Problem Statement

Write a Python program to generate and print the **Fibonacci Sequence** up to the `n`-th number (inclusive) using **list comprehension**. The Fibonacci sequence is computed based on the following formula:

- f(n) = 0 if n = 0
- f(n) = 1 if n = 1
- f(n) = f(n-1) + f(n-2) if n > 1

---

## 🧠 Concepts Used

- Fibonacci sequence calculation
- List comprehension
- Conditional logic
- `str.join()` for formatted output

---

## 🧪 Sample Code

```python
def fibonacci(n):
    fib_sequence = [0, 1] + [0]*(n-1)
    [fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for i in range(2, n)]
    return fib_sequence[:n]

# Input from user
n = int(input("Enter the value of n: "))

# Generating Fibonacci sequence using list comprehension
fib_nums = [str(num) for num in fibonacci(n)]
print(",".join(fib_nums))
```

---

## 🎯 Example Input & Output

### Input

```
Enter the value of n: 8
```

### Output

```
0,1,1,2,3,5,8,13
```

---

## ✅ Notes

- The program uses a list comprehension to generate the Fibonacci sequence.
- The `fibonacci()` function generates the sequence by iterating through the previous two values and adding them.
- The sequence is printed in a comma-separated format using `",".join()`.

---
