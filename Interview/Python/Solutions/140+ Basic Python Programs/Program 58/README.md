
# 📝 Program 58: Cloning or Copying a List (Python)

This Python program demonstrates different ways to **clone** or **copy** a list so changes to one list don’t affect the other.

---

## 📌 Problem Statement

**Write a Python program to clone or copy a list.**

---

## 💡 Understanding the Problem

In Python, assigning a list to another variable using `=` does **not** create a new list—it just creates a new reference to the same list.

To truly **copy or clone a list**, we use various methods:

---

## ✅ Sample Code

```python
# Original list
original_list = [10, 20, 30, 40, 50]

# Method 1: Using list slicing
cloned_list1 = original_list[:]

# Method 2: Using the list() constructor
cloned_list2 = list(original_list)

# Method 3: Using copy() method
cloned_list3 = original_list.copy()

# Display the results
print("Original List:", original_list)
print("Cloned List using slicing:", cloned_list1)
print("Cloned List using list():", cloned_list2)
print("Cloned List using copy():", cloned_list3)
```

---

## ▶️ Example Output

```bash
Original List: [10, 20, 30, 40, 50]
Cloned List using slicing: [10, 20, 30, 40, 50]
Cloned List using list(): [10, 20, 30, 40, 50]
Cloned List using copy(): [10, 20, 30, 40, 50]
```

---

## 🧠 Note

- All three methods create a **shallow copy**.
- Changes to one list **do not affect** the cloned copy.
- For **nested lists**, use the `copy` module's `deepcopy()`.

---

## 🧪 Try It Yourself

- Clone a nested list and test if the inner list is affected.
- Use user input to create and clone a list.
- Compare object IDs with `id()` to prove the lists are different objects.

---

