
# 📘 Program 108: Reverse a Boolean Value

## 🧮 Description

This Python program defines a function that takes a boolean value as input and reverses it. If the input is not a boolean (`True` or `False`), the function returns the string `"boolean expected"`. This is a simple exercise to check data types and reverse boolean values.

---

## 📌 Function Definition

```python
def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"
```

---

## ✅ Examples

```python
print(reverse(True))     # ➞ False
print(reverse(False))    # ➞ True
print(reverse(0))        # ➞ "boolean expected"
print(reverse(None))     # ➞ "boolean expected"
```

### 💡 Output

```
False
True
boolean expected
boolean expected
```

---

## 📂 Use Cases

- **Boolean Manipulation**: Reversing boolean values is commonly used in logical operations.
- **Data Type Checking**: Verifying that the input is of the expected type (boolean) before performing an operation.
- **Error Handling**: Returning a custom error message when the wrong type of data is passed.

---

## 🛡️ Notes

- The function checks if the input is of the `bool` type. If not, it returns `"boolean expected"`.
- Only the boolean values `True` and `False` will have their values reversed.
- Any non-boolean values like integers, `None`, strings, etc., will return the custom error message.

---

