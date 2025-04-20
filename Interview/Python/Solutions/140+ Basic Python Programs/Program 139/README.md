
## 📘 Program 139 – Create a Dictionary with Upper and Lower Case Letters

### 📝 Description  

This program defines a function `mapping()` that takes a list of lowercase letters and returns a dictionary where each key is the lowercase version of a letter and each value is the uppercase version of that letter.

### ✅ Examples

```python
mapping(["p", "s"])
# ➞ { "p": "P", "s": "S" }

mapping(["a", "b", "c"])
# ➞ { "a": "A", "b": "B", "c": "C" }

mapping(["a", "v", "y", "z"])
# ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
```

---

### 🧠 Function Logic

- **mapping(letters)**:
  - The function takes a list of lowercase letters as input.
  - It creates a dictionary where each key is a lowercase letter from the list, and its corresponding value is the uppercase version of that letter.

---

### 🧠 Function Definition

```python
def mapping(letters):
    # Create a dictionary where each key is a letter and its value is the uppercase version
    return {letter: letter.upper() for letter in letters}
```

---

### 🔁 How to Use

1. Pass a list of lowercase letters to the `mapping()` function.
2. The function will return a dictionary where each lowercase letter is mapped to its uppercase counterpart.

### 💡 Example Usage

```python
# Input list of lowercase letters
letters = ["p", "s"]

# Call the function
result = mapping(letters)

# Output the result
print(result)  # Output: {'p': 'P', 's': 'S'}
```

---

### 🧠 Example Walkthrough

For the input `["a", "b", "c"]`:

- The function will return the dictionary `{"a": "A", "b": "B", "c": "C"}`.

For the input `["a", "v", "y", "z"]`:

- The function will return the dictionary `{"a": "A", "v": "V", "y": "Y", "z": "Z"}`.

---

### 🧠 Additional Notes

- The input list will always contain lowercase letters, so no need to handle uppercase letters.
- The function uses dictionary comprehension to create the dictionary efficiently.

---

### 🔍 Example Input/Output

- **Input**: `["p", "s"]`
  - **Output**: `{"p": "P", "s": "S"}`

- **Input**: `["a", "v", "y", "z"]`
  - **Output**: `{"a": "A", "v": "V", "y": "Y", "z": "Z"}`
