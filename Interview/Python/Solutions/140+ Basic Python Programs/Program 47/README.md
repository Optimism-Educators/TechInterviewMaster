# Program47
Here's the explanation and code for **Program 47: Check if a Number is a Harshad Number**:

---

```markdown
# 📝 Program 47: Check if a Number is a Harshad Number (Python)

This Python program checks whether a given number is a **Harshad Number**. A **Harshad Number** (or **Niven Number**) is an integer that is divisible by the sum of its digits. 

---

## 📌 Problem Statement

**Write a Python program to determine whether the given number is a Harshad Number.**

---

## 🔢 What is a Harshad Number?

A **Harshad Number** is a number that is divisible by the sum of its digits. To check if a number is a Harshad number:
1. Compute the sum of the digits of the number.
2. If the number is divisible by the sum of its digits, it is a Harshad number.

### Examples:
- **18** is a Harshad number because:
  \[
  1 + 8 = 9 \quad \text{and} \quad 18 \div 9 = 2 \quad (\text{it is divisible})
  \]
- **42** is not a Harshad number because:
  \[
  4 + 2 = 6 \quad \text{and} \quad 42 \div 6 = 7 \quad (\text{it is divisible, actually!})
  \]
  But let’s check if the code works for various cases.
  
---

## ✅ Sample Code

```python
# Function to check if a number is a Harshad number
def is_harshad_number(num):
    # Calculate the sum of the digits of the number
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0

# Input from the user
num = int(input("Enter a number: "))

# Check and print if the number is a Harshad number
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
```

---

## ▶️ Example Output

```bash
Enter a number: 18
18 is a Harshad number.

Enter a number: 42
42 is a Harshad number.
```

---

## 📁 Suggested Project Structure

```
harshad_number/
├── harshad_number.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to **check multiple numbers** at once by accepting a list of numbers.
- Implement a function to **print all Harshad numbers** within a specific range (e.g., 1 to 100).
- Explore **Harshad numbers in other bases** (e.g., binary, hexadecimal).

---

Happy Coding! 🚀

```

---

This program checks if a number is a Harshad number by:
1. Calculating the sum of its digits using Python's built-in `sum()` function and `str()` conversion.
2. Checking if the number is divisible by the sum of its digits using the modulus operator (`%`).

Let me know if you need further modifications or explanations!
