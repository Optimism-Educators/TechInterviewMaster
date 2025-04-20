# Program26
Absolutely! Here's a detailed and well-structured `README.md` for **Program 26 – Simple Calculator in Python**:

---

```markdown
# ➕ Program 26: Simple Calculator (Python)

This Python program functions as a basic calculator that performs **four mathematical operations**: **Addition, Subtraction, Multiplication, and Division**.

---

## 📌 Problem Statement

**Write a Python program to create a simple calculator that can perform basic arithmetic operations.**

---

## 🧮 Basic Mathematical Operations

The calculator should handle:

| Operation      | Symbol | Example             |
|----------------|--------|---------------------|
| Addition       | `+`    | 5 + 3 = 8           |
| Subtraction    | `-`    | 10 - 4 = 6          |
| Multiplication | `*`    | 6 * 7 = 42          |
| Division       | `/`    | 20 / 4 = 5.0        |

---

## ✅ Python Code

```python
# Simple Calculator in Python

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# User interface
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

# Input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation
if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid Input")
```

---

## ▶️ Example Output

```bash
Select operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
Enter choice (1/2/3/4): 3
Enter first number: 9
Enter second number: 6
Result: 54.0
```

---

## 📁 Suggested Project Structure

```
simple_calculator/
├── calculator.py
└── README.md
```

---

## 🧠 You Can Try

- Handle division by zero with custom error messages ✅
- Use a `while` loop to repeat calculations until the user exits 🔁
- Add a menu to perform more operations like modulus or power 🔢

---
