# Program130
Here is the **README.md** file for **Program 130 – Remove Duplicates and Sort List**:

---

## 📘 Program 130 – Remove Duplicates and Sort List

### 📝 Description  

This program defines a function `setify()` that takes a list of numbers as input, removes any duplicate elements, and returns a sorted list with the remaining unique elements. The function essentially transforms the list into a set (to eliminate duplicates) and then sorts the set to return a list.

### 🔍 Purpose  

The function ensures that all duplicate elements are removed from the input list and that the resulting list is sorted in ascending order. This function is useful for creating a list of unique values from an unordered collection of numbers.

---

### ✅ Examples

```python
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

setify([4, 4, 4, 4]) ➞ [4]

setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
```

---

### 💡 Function Logic

1. **Input**: The function takes a list of numbers as input.
2. **Process**:
   - Convert the list to a set to automatically remove duplicates.
   - Convert the set back to a list.
   - Sort the list in ascending order.
3. **Return**: The function returns a sorted list with unique elements.

---

### 🧠 Function Definition

```python
def setify(lst):
    # Remove duplicates by converting to a set, then sort and return the list
    return sorted(list(set(lst)))
```

---

### 🔁 How to Use

1. Call the `setify()` function with a list of numbers as input.
2. The function will return a sorted list containing only the unique elements from the original list.

### 💡 Example Usage

```python
result = setify([1, 3, 3, 5, 5])
print(result)  # Output: [1, 3, 5]
```

---

### 🧠 Example Walkthrough

For the input `[1, 3, 3, 5, 5]`:

- The function first removes duplicates by converting the list to a set: `{1, 3, 5}`.
- Then, it converts the set back to a list: `[1, 3, 5]`.
- Finally, it sorts the list: `[1, 3, 5]`.

For the input `[4, 4, 4, 4]`:

- The function removes duplicates: `{4}`.
- It converts it back to a list: `[4]`.
- The list is already sorted: `[4]`.

---

### 🧠 Additional Notes

- **Edge Cases**:
  - If the input list contains only duplicate elements, the output will have just one element.
  - If the input list is already sorted and has no duplicates, the function will return the list unchanged.

---

### 🔍 Example Input/Output

- **Input**: `[1, 3, 3, 5, 5]`
  - **Output**: `[1, 3, 5]`
  
- **Input**: `[4, 4, 4, 4]`
  - **Output**: `[4]`
  
- **Input**: `[5, 7, 8, 9, 10, 15]`
  - **Output**: `[5, 7, 8, 9, 10, 15]`

- **Input**: `[3, 3, 3, 2, 1]`
  - **Output**: `[1, 2, 3]`

---

Let me know if you need any further modifications!
