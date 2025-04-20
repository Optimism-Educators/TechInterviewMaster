
# 📝 Program 59: Count Occurrences of an Element in a List (Python)

This Python program demonstrates how to **count the number of times a specific element appears in a list**.

---

## 📌 Problem Statement

**Write a Python program to count the occurrences of a specific element in a list.**

---

## 💡 Understanding the Problem

In Python, lists can contain duplicate elements. To determine **how many times** a particular element appears in the list, we can use:

- The built-in `count()` method of a list.

---

## ✅ Sample Code

```python
# Define a list
sample_list = [1, 2, 3, 4, 2, 3, 2, 5, 6, 2]

# Ask the user for the element to count
element = int(input("Enter the element to count: "))

# Count occurrences using count() method
count = sample_list.count(element)

# Display the result
print(f"The element {element} appears {count} times in the list.")
```

---

## ▶️ Example Output

```bash
Enter the element to count: 2
The element 2 appears 4 times in the list.
```

---

## 🧠 Note

- `count()` works for **integers**, **strings**, and even **custom objects**.
- It's **case-sensitive** when used on lists of strings.

---

## 🧪 Try It Yourself

- Use a list of strings and count how many times a word appears.
- Write a function that returns the count of any element in a given list.

---
