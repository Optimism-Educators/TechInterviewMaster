
# 📝 Program 69: Merging Two Dictionaries (Python)

This Python program demonstrates how to merge two dictionaries into one.

---

## 📌 Problem Statement

**Write a Python program to merge two dictionaries.**

---

## 💡 What is Dictionary Merging?

Dictionary merging refers to the process of combining two dictionaries into a single dictionary. If both dictionaries have the same key, the values from the second dictionary will overwrite the values from the first dictionary.

---

## ✅ Sample Code

```python
# Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    # Merge dict2 into dict1 using the update() method
    dict1.update(dict2)
    return dict1

# Input dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'d': 40, 'e': 50}

# Merge the dictionaries
merged_dict = merge_dicts(dict1, dict2)

# Print the merged dictionary
print("Merged Dictionary:", merged_dict)
```

---

## ▶️ Example Output

```bash
Merged Dictionary: {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
```

---

## 🔍 Explanation

1. **`update()` Method**: The `update()` method is used to merge `dict2` into `dict1`. If `dict1` and `dict2` have any common keys, the value from `dict2` will overwrite the corresponding value in `dict1`.
2. **Merging**: The function `merge_dicts` performs the merging of two dictionaries.
3. **Result**: The merged dictionary contains all key-value pairs from both dictionaries.

---
