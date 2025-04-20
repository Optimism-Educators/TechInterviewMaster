
# 📝 Program 58: Cloning or Copying a List in Python

This program demonstrates how to **clone** or **copy** a list in Python using various methods.

---

## 📌 Problem Statement

**Write a Python program to create a copy (clone) of a list.**

---

## 💡 Understanding the Problem

When working with lists, it's important to distinguish between **copying** and **referencing**.  
If you simply assign one list to another, they both point to the same memory location (i.e., they are references).  
To make a true clone, you must **explicitly copy the contents**.

---

## ✅ Sample Code

```python
# Original list
original_list = [10, 20, 30, 40, 50]

# Method 1: Using list slicing
cloned_list1 = original_list[:]

# Method 2: Using list() constructor
cloned_list2 = list(original_list)

# Method 3: Using the copy() method (Python 3.3+)
cloned_list3 = original_list.copy()

# Output
print("Original List:", original_list)
print("Cloned List (Method 1):", cloned_list1)
print("Cloned List (Method 2):", cloned_list2)
print("Cloned List (Method 3):", cloned_list3)
```

---

## ▶️ Example Output

```bash
Original List: [10, 20, 30, 40, 50]
Cloned List (Method 1): [10, 20, 30, 40, 50]
Cloned List (Method 2): [10, 20, 30, 40, 50]
Cloned List (Method 3): [10, 20, 30, 40, 50]
```

---

## 🧠 Notes

- `cloned_list1 = original_list[:]` creates a **shallow copy** using slicing.
- `cloned_list2 = list(original_list)` creates a new list object with the same elements.
- `cloned_list3 = original_list.copy()` uses the built-in method available in Python 3.3+.

---

## 🛠 Bonus Tip

For nested lists (lists within lists), use the `copy` module to make a **deep copy**:

```python
import copy
deep_cloned_list = copy.deepcopy(original_list)
```

---
