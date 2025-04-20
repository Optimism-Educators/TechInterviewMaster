# Program25
Here’s a polished and educational `README.md` file for **Program 25 – Find ASCII Value of a Character in Python**:

---

```markdown
# 🔤 Program 25: Find ASCII Value of a Character (Python)

This Python program takes a **single character** as input and returns its **ASCII value** using the built-in `ord()` function.

---

## 📌 Problem Statement

**Write a Python Program to Find the ASCII Value of a Character.**

---

## 🔠 What is ASCII?

**ASCII** stands for **American Standard Code for Information Interchange**.  
It is a **character encoding standard** used to represent characters using numeric codes.

### 📊 ASCII Value Range:

- **7-bit ASCII**: Values range from **0 to 127**
- **Extended ASCII (8-bit)**: Values range from **0 to 255**

Each value represents a character, including:
- Alphabets (A–Z, a–z)
- Digits (0–9)
- Symbols (!, @, #, etc.)
- Control characters (like newline `\n`)

### 🔎 Examples:

| Character | ASCII Value |
|-----------|-------------|
| A         | 65          |
| a         | 97          |
| 0         | 48          |
| $         | 36          |

---

## ✅ Python Code

```python
# Python program to find the ASCII value of a character

# Taking input from user
char = input("Enter a character: ")

# Validate single character input
if len(char) == 1:
    print(f"The ASCII value of '{char}' is {ord(char)}")
else:
    print("Please enter only a single character.")
```

---

## ▶️ Example Output

```bash
Enter a character: A
The ASCII value of 'A' is 65
```

---

## 🔧 Python Built-in Function Used

- `ord(character)` – Returns the ASCII (or Unicode) value of the input character.
- `chr(number)` – (Opposite of `ord()`) Returns the character corresponding to an ASCII/Unicode number.

---

## 📁 Suggested File Structure

```
ascii_value/
├── ascii_value.py
└── README.md
```

---

## 💡 Try This Too

- Use `chr()` to convert an ASCII value back to a character.
- Build a table of ASCII values using a loop.

```python
# Display ASCII values for characters A-Z
for ch in range(65, 91):
    print(f"{chr(ch)} : {ch}")
```

---

