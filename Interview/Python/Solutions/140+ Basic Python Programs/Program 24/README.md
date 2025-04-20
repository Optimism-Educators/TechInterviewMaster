# Program24
Here's a well-organized and student-friendly `README.md` for **Program 24 – Convert Decimal to Binary, Octal, and Hexadecimal**:

---

```markdown
# 🔢 Program 24: Convert Decimal to Binary, Octal, and Hexadecimal

This Python program converts a **decimal number** into its **binary**, **octal**, and **hexadecimal** representations.

---

## 📌 Problem Statement

**Write a Python Program to Convert a Decimal Number to Binary, Octal, and Hexadecimal.**

---

## 🧠 Concept Overview

A **decimal number** (base 10) can be converted to:
- **Binary** (base 2)
- **Octal** (base 8)
- **Hexadecimal** (base 16)

These conversions can be done using either **manual methods** or **built-in Python functions**.

---

## 🔍 Manual Conversion (Example for Decimal 27)

### 1️⃣ Binary Conversion (Base 2)
```

27 ÷ 2 = 13 remainder 1  
13 ÷ 2 = 6  remainder 1  
6 ÷ 2  = 3  remainder 0  
3 ÷ 2  = 1  remainder 1  
1 ÷ 2  = 0  remainder 1  

```
📌 Binary (bottom to top): `11011`

### 2️⃣ Octal Conversion (Base 8)
```

27 ÷ 8 = 3 remainder 3  
3 ÷ 8  = 0 remainder 3  

```
📌 Octal: `33`

### 3️⃣ Hexadecimal Conversion (Base 16)
```

27 ÷ 16 = 1 remainder 11 (B in hexadecimal)  

```
📌 Hexadecimal: `1B`

---

## ✅ Python Code

```python
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# Input from user
dec = int(input("Enter a decimal number: "))

print("The decimal number is:", dec)
print("Binary format:", bin(dec)[2:])        # Remove '0b' prefix
print("Octal format:", oct(dec)[2:])         # Remove '0o' prefix
print("Hexadecimal format:", hex(dec)[2:].upper())  # Remove '0x' and uppercase
```

---

## ▶️ Example Output

```bash
Enter a decimal number: 27
The decimal number is: 27
Binary format: 11011
Octal format: 33
Hexadecimal format: 1B
```

---

## 💡 Extra Tips

- Use `bin()`, `oct()`, and `hex()` functions for quick conversion.
- To manually convert, divide by the target base and record the remainders.

---

## 📁 Suggested File Structure

```
decimal_converter/
├── converter.py
└── README.md
```

---

## 🧪 Try It Yourself

- Convert different decimal numbers and verify using manual steps.
- Extend the program to convert in the reverse direction (binary to decimal).

---

Happy Learning! 💻🧠

```

Let me know if you'd like this turned into a project folder with files automatically generated!
