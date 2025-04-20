# Program103
Sure! Here's **Program 103** in the same format as you've been using:

---

```markdown
# 🟩 Program 103: Reverse String with Opposite Case

This Python program takes a string as input and returns it **reversed**, with each character’s case **inverted** (uppercase to lowercase and vice versa).

---

## 📌 Problem Statement

Create a function that takes a **string** and returns:

- The **reversed string**
- With the **opposite case** for each character

---

## 🧪 Examples

### Input:
```python
reverse("Hello World")
reverse("ReVeRsE")
reverse("Radar")
```

### Output

```
DLROw OLLEh
eSrEvEr
RADAr
```

---

## 🧠 Concepts Used

- String slicing for reversing: `[::-1]`
- String method `.swapcase()` for inverting the case

---

## ✅ Constraints

- Input is a string with any mix of upper/lower case characters and spaces.
- Output should maintain the same characters but with case flipped and order reversed.

---

## 🧪 Sample Code

```python
def reverse(txt):
    return txt[::-1].swapcase()

# Test cases
print(reverse("Hello World"))  # ➞ "DLROw OLLEh"
print(reverse("ReVeRsE"))      # ➞ "eSrEvEr"
print(reverse("Radar"))        # ➞ "RADAr"
```

---

## 🎯 Output Explanation

- `"Hello World"` → reversed → `"dlroW olleH"` → swapcase → `"DLROw OLLEh"`
- `"ReVeRsE"` → reversed → `"EsReVeR"` → swapcase → `"eSrEvEr"`
- `"Radar"` → reversed → `"radaR"` → swapcase → `"RADAr"`

---
