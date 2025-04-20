
# 🟩 Program 96: Decimal to Binary Conversion

This Python program converts a decimal (base-10) number into its binary (base-2) representation.

---

## 📌 Problem Statement

The task is to write a function that converts a given decimal (base-10) number into its binary (base-2) equivalent. The conversion is straightforward: starting from the rightmost bit, each bit's value is doubled as you move to the left.

### Example:

For `decimal = 1`:
- The binary representation is `"1"`.

For `decimal = 5`:
- The binary representation is `"101"`.

For `decimal = 10`:
- The binary representation is `"1010"`.

---

## 🧠 Concepts Used

- Binary Representation
- Integer Division and Modulo Operations

---

## 🧪 Sample Code

```python
def binary(decimal):
    return bin(decimal)[2:]

# Test cases
print(binary(1))   # Output: "1"
print(binary(5))   # Output: "101"
print(binary(10))  # Output: "1010"
```

---

## 🎯 Example Input & Output

### Input

```
1
5
10
```

### Output

```
"1"
"101"
"1010"
```

---

## ✅ Notes

- The function `bin()` returns the binary representation of a number, but it includes a prefix `"0b"`. To remove the prefix, we slice the string with `[2:]`.
- The binary representation is returned as a string.

---