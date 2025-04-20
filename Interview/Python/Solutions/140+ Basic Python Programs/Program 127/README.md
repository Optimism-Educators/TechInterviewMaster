
## 📘 Program 127 – Symmetrical Number Checker

### 📝 Description  

This program defines a function `is_symmetrical(n)` that checks if a given number is symmetrical. A number is considered symmetrical if it is the same as its reverse. The function returns `True` if the number is symmetrical, and `False` otherwise.

### 🔍 Purpose  

The function checks whether a given number reads the same forwards and backwards. It compares the number with its reverse to determine if it's symmetrical.

---

### ✅ Examples

```python
is_symmetrical(7227) ➞ True    # Number is symmetrical

is_symmetrical(12567) ➞ False  # Number is not symmetrical

is_symmetrical(44444444) ➞ True  # Number is symmetrical

is_symmetrical(9939) ➞ False  # Number is not symmetrical

is_symmetrical(1112111) ➞ True  # Number is symmetrical
```

---

### 💡 Function Logic

1. **Input**: The function takes a number `n` as input.
2. **Process**:
   - Convert the number to a string.
   - Check if the number is equal to its reverse.
3. **Return**: The function returns `True` if the number is symmetrical, and `False` otherwise.

---

### 🧠 Function Definition

```python
def is_symmetrical(n):
    # Convert the number to string and check if it equals its reverse
    return str(n) == str(n)[::-1]
```

---

### 🔁 How to Use

1. Call the `is_symmetrical()` function with a number as the argument.
2. The function will return `True` if the number is symmetrical and `False` if it is not.

### 💡 Example Usage

```python
result = is_symmetrical(7227)
print(result)  # Output: True
```

---

### 🧠 Example Walkthrough

For the input `7227`, the function follows these steps:

- Convert the number to a string: `"7227"`.
- Reverse the string: `"7227"`.
- Since the original string is the same as the reversed string, the function returns `True`.

For the input `12567`, the function compares:

- Convert the number to a string: `"12567"`.
- Reverse the string: `"76521"`.
- Since the original string is different from the reversed string, the function returns `False`.

---

### 🛠️ How It Works

- **String Conversion**: The number is converted to a string to facilitate comparison.
- **Reverse String**: The reverse of the string is obtained using Python slicing (`[::-1]`).
- **Comparison**: The function checks if the string is equal to its reversed version.

---

### 🔍 Example Input/Output

- **Input**: `7227`
  - **Output**: `True`
  
- **Input**: `12567`
  - **Output**: `False`
  
- **Input**: `44444444`
  - **Output**: `True`

