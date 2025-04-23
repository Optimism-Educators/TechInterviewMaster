
## 📘 Program 117 – Update List with Next in Line

### 📝 Description  

This program defines a function `next_in_line(lst, num)` that updates a given list by performing two actions:

1. Adds a number to the end of the list.
2. Removes the first element from the list.

If the list is empty, the function returns the message `"No list has been selected"`.

---

### ✅ Examples

```python
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42], 6) ➞ [10, 20, 42, 6]
next_in_line([], 6) ➞ "No list has been selected"
```

---

### 🧠 Function Logic

- Check if the list is empty.  
  - If yes, return `"No list has been selected"`.
- Else:
  - Append the new number to the end.
  - Remove the first element.
  - Return the modified list.

---

### 💡 Function Definition

```python
def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    lst.append(num)
    lst.pop(0)
    return lst
```

---

### 🔁 How to Use

1. Provide a list of values and a number you want to add.
2. Call the `next_in_line()` function with those arguments.
3. Receive the updated list (or an error message if the list is empty).
