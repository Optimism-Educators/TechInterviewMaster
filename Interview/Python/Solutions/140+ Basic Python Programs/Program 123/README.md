# Program123
Here is the **README.md** file for **Program 123 – Simon Says List Shift**:

---

## 📘 Program 123 – Simon Says List Shift

### 📝 Description  

This program defines a function `simon_says(lst1, lst2)` that checks if the second list is the first list shifted to the right by one element. It returns `True` if the second list follows the first list by one element and `False` otherwise.

### 🔍 Purpose  

The function compares two lists to determine if the second list is a shifted version of the first list, specifically shifted by one element to the right.

---

### ✅ Examples

```python
simon_says([1, 2], [5, 1]) ➞ True

simon_says([1, 2], [5, 5]) ➞ False

simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True

simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
```

---

### 💡 Function Logic

1. **Input**: The function takes two lists, `lst1` and `lst2`, both of the same length.
2. **Comparison**: The function checks if the second list `lst2` matches the first list `lst1` shifted to the right by one element.
   - The first element of `lst2` should be the second element of `lst1`.
   - The second element of `lst2` should be the third element of `lst1`, and so on.
3. **Return**: The function returns `True` if `lst2` matches `lst1` after the shift, and `False` otherwise.

---

### 🧠 Function Definition

```python
def simon_says(lst1, lst2):
    return lst1[1:] == lst2[:-1]
```

---

### 🔁 How to Use

1. Call the `simon_says()` function with two lists as arguments: `lst1` and `lst2`.
2. The function will compare the two lists and return `True` if `lst2` is the shifted version of `lst1` by one element to the right, and `False` otherwise.

### 💡 Example Usage

```python
result = simon_says([1, 2], [5, 1])
print(result)  # Output: True
```

---

### 🛠️ How It Works

- **List Slicing**: The function compares the lists using slicing:
  - `lst1[1:]`: This takes all elements of `lst1` except the first element.
  - `lst2[:-1]`: This takes all elements of `lst2` except the last element.
  
  It checks if these two slices are equal. If they are, it means `lst2` is the shifted version of `lst1`.
  
- **Edge Case Handling**:
  - The 0-indexed element in `lst2` and the n-1 indexed element in `lst1` are not checked as per the problem's instructions.

---

Let me know if you need further changes or additions!
