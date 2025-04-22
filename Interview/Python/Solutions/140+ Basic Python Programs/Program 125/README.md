
## 📘 Program 125 – Isogram Checker

### 📝 Description  

This program defines a function `is_isogram(word)` that checks whether a given word is an **isogram**. An **isogram** is a word that has no duplicate letters, regardless of case.

### 🔍 Purpose  

The function checks whether a word contains unique characters, ignoring letter case. It returns `True` if the word is an isogram and `False` if there are any duplicate letters.

---

### ✅ Examples

```python
is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False  # case insensitive check

is_isogram("Consecutive") ➞ False
```

---

### 💡 Function Logic

1. **Input**: The function takes a string `word` as input.
2. **Process**:
   - Convert the word to lowercase to make it case-insensitive.
   - Check if any characters repeat by comparing the length of the set (which removes duplicates) and the original word.
3. **Return**: The function returns `True` if no duplicates are found (isogram), otherwise returns `False`.

---

### 🧠 Function Definition

```python
def is_isogram(word):
    # Convert the word to lowercase and check if there are any repeating characters
    word = word.lower()  # Ignore case sensitivity
    return len(word) == len(set(word))
```

---

### 🔁 How to Use

1. Call the `is_isogram()` function with a string as the argument.
2. The function will return `True` if the string is an isogram, and `False` otherwise.

### 💡 Example Usage

```python
result = is_isogram("Algorism")
print(result)  # Output: True
```

---

### 🧠 Example Walkthrough

For the input `"PasSword"`, the function follows these steps:

- Convert the word to lowercase: `"password"`.
- Convert the word into a set of unique characters: `{"p", "a", "s", "w", "o", "r", "d"}`.
- The length of the set (`7`) is less than the length of the word (`8`), indicating that there are repeated characters.
- The function returns `False`.

---

### 🛠️ How It Works

- **Lowercase Conversion**: The `word.lower()` function makes the check case-insensitive.
- **Set Usage**: By converting the word into a set, we remove duplicate letters. If the length of the set is equal to the length of the word, it indicates that the word is an isogram.

---

### 🔍 Example Input/Output

- **Input**: `"Algorism"`
  - **Output**: `True`
  
- **Input**: `"PasSword"`
  - **Output**: `False`
  
- **Input**: `"Consecutive"`
  - **Output**: `False`


