# Program121
Here’s the **README.md** file for **Program 121 – Return Only Integers**:

---

## 📘 Program 121 – Return Only Integers

### 📝 Description  

This program defines a function `return_only_integer(lst)` that filters a list of mixed elements (integers, strings, booleans, etc.) and returns a new list containing only the integers from the original list.

### 🔍 Purpose  

The function's purpose is to extract and return all integer values from a list, ignoring other types of data such as strings, floats, or booleans.

---

### ✅ Examples

```python
return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]

return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]

return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]

return_only_integer(["String", True, 3.3, 1]) ➞ [1]
```

---

### 💡 Function Logic

1. **Input**: The user provides a list `lst` that may contain integers, strings, booleans, or other elements.
2. **Filtering**: The function iterates over the list and filters out elements that are not integers.
3. **Return**: The function returns a new list containing only the integers found in the original list.

---

### 🧠 Function Definition

```python
def return_only_integer(lst):
    return [x for x in lst if isinstance(x, int)]
```

---

### 🔁 How to Use

1. Call the `return_only_integer()` function with a list as input.
   - The input list may contain various types of elements such as integers, strings, booleans, etc.
2. The function will return a new list containing only the integer values from the input list.

### 💡 Example Usage

```python
result = return_only_integer([9, 2, "space", "car", "lion", 16])
print(result)  # Output: [9, 2, 16]
```

---

### 🛠️ How It Works

- **isinstance()** is used to check whether each element in the list is an integer.
- The list comprehension filters out non-integer elements and returns only integers.

---

Let me know if you need any other adjustments!
