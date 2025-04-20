
# 📘 Program 107: Double Characters in a String

## 🧮 Description

This Python program defines a function that takes a string as input and returns a new string in which each character from the original string is repeated once. This is a simple string manipulation exercise to practice iterating over characters in a string.

---

## 📌 Function Definition

```python
def double_char(string):
    return ''.join([char * 2 for char in string])
```

---

## ✅ Examples

```python
print(double_char("String"))        # ➞ "SSttrriinngg"
print(double_char("Hello World!"))  # ➞ "HHeelllloo WWoorrlldd!!"
print(double_char("1234! "))        # ➞ "11223344!! "
```

### 💡 Output

```
SSttrriinngg
HHeelllloo WWoorrlldd!!
11223344!! 
```

---

## 📂 Use Cases

- String manipulation for text processing
- Learning how to work with string iteration and list comprehension
- A simple way to double characters in strings for various applications

---

## 🛡️ Notes

- The function handles both alphabets, numbers, and special characters.
- White spaces are also repeated if they appear in the string.

---

