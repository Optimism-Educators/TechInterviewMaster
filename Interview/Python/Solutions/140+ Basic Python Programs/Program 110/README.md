
# 📘 Program 110: Find Indices of Capital Letters in a String

## 🧮 Description

This Python program defines a function that takes a single string as input and returns an ordered list containing the indices of all the capital letters in the string.

### Functionality:
- The function loops through the string and checks each character to see if it is a capital letter.
- It returns a list of indices where capital letters are located.

---

## 📌 Function Definition

```python
def index_of_caps(string):
    return [i for i, char in enumerate(string) if char.isupper()]
```

### How it Works

- The function uses a list comprehension to iterate through the string.
- `enumerate(string)` provides both the index (`i`) and the character (`char`) for each position in the string.
- `char.isupper()` checks if the character is an uppercase letter.
- If the character is uppercase, its index is added to the resulting list.

---

## ✅ Examples

```python
print(index_of_caps("eDaBiT"))     # ➞ [1, 3, 5]
print(index_of_caps("eQuINoX"))    # ➞ [1, 3, 4, 6]
print(index_of_caps("determine"))  # ➞ []
print(index_of_caps("STRIKE"))     # ➞ [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))        # ➞ [1]
```

### 💡 Output

```
[1, 3, 5]
[1, 3, 4, 6]
[]
[0, 1, 2, 3, 4, 5]
[1]
```

---

## 📂 Use Cases

- **Text Analysis**: Useful for analyzing capitalized words or letters in text processing tasks.
- **Formatting and Styling**: Can be used for tasks where capitalized words need to be located or processed (e.g., for certain styles in text).
- **Learning String Operations**: A great example of working with strings and understanding how to manipulate them with basic Python functions.

---

## 🛡️ Notes

- The function is case-sensitive and only detects uppercase letters (A-Z).
- The result is an ordered list of indices where capital letters are located in the given string.
- It returns an empty list if no capital letters are found.

---

## ✨ Author

Program created for basic Python learning and practice.

```

---

Let me know if you'd like to save this as a `.md` file or if you'd like to include it in your project!
