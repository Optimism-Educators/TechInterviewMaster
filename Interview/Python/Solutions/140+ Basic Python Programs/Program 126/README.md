# Program126
Here is the **README.md** file for **Program 126 – String Order Checker**:

---

## 📘 Program 126 – String Order Checker

### 📝 Description  

This program defines a function `is_in_order(s)` that checks whether the characters of a given string are in lexicographical (alphabetical or numerical) order. The function returns `True` if the characters of the string are in order, and `False` otherwise.

### 🔍 Purpose  

The function checks if each character in the string follows the order of the previous one. The function supports both alphabetic and numeric strings.

---

### ✅ Examples

```python
is_in_order("abc") ➞ True  # Characters in alphabetical order

is_in_order("edabit") ➞ False  # Characters are not in order

is_in_order("123") ➞ True  # Characters in numerical order

is_in_order("xyzz") ➞ True  # Characters in order with repeated letters
```

---

### 💡 Function Logic

1. **Input**: The function takes a string `s` as input.
2. **Process**:
   - Check if each character is lexicographically greater than or equal to the previous character.
   - The comparison is done character by character.
3. **Return**: The function returns `True` if the characters are in order, and `False` otherwise.

---

### 🧠 Function Definition

```python
def is_in_order(s):
    # Check if each character is greater than or equal to the previous one
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))
```

---

### 🔁 How to Use

1. Call the `is_in_order()` function with a string as the argument.
2. The function will return `True` if the characters are in order and `False` if they are not.

### 💡 Example Usage

```python
result = is_in_order("abc")
print(result)  # Output: True
```

---

### 🧠 Example Walkthrough

For the input `"edabit"`, the function follows these steps:

- Compare each character with the previous one:
  - `'e' <= 'd'` is False.
- Since the characters are not in order, the function returns `False`.

For the input `"abc"`, the function compares:

- `'a' <= 'b'` is True.
- `'b' <= 'c'` is True.
- Since all comparisons are True, the function returns `True`.

---

### 🛠️ How It Works

- **String Comparison**: The function uses a list comprehension with `all()` to check that every character is less than or equal to the next character in the string.
- **Lexicographical Order**: The function works for both alphabetic and numeric characters.

---

### 🔍 Example Input/Output

- **Input**: `"abc"`
  - **Output**: `True`
  
- **Input**: `"edabit"`
  - **Output**: `False`
  
- **Input**: `"123"`
  - **Output**: `True`

---

Let me know if you need any further modifications!
