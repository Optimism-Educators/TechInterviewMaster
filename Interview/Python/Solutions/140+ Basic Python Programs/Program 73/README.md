
# 📝 Program 73: Sort Python Dictionaries by Key or Value

This Python program demonstrates how to sort a dictionary by either its keys or its values.

---

## 📌 Problem Statement

**Write a Python program to sort Python Dictionaries by Key or Value.**

---

## 💡 Sorting Dictionaries

Dictionaries in Python are unordered collections by default. However, you can sort them either by key or by value using built-in Python functions like `sorted()`. Sorting helps when you want to organize data in a more readable or meaningful way.

---

## ✅ Sample Code

```python
# Sorting dictionary by Key
def sort_dict_by_key(input_dict):
    sorted_dict_by_key = dict(sorted(input_dict.items()))
    return sorted_dict_by_key

# Sorting dictionary by Value
def sort_dict_by_value(input_dict):
    sorted_dict_by_value = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict_by_value

# Sample dictionary
input_dict = {'apple': 10, 'banana': 3, 'orange': 7, 'grapes': 5}

# Test the functions
print("Original Dictionary:", input_dict)

# Sorted by Key
print("\nSorted by Key:", sort_dict_by_key(input_dict))

# Sorted by Value
print("\nSorted by Value:", sort_dict_by_value(input_dict))
```

---

## ▶️ Example Output

```bash
Original Dictionary: {'apple': 10, 'banana': 3, 'orange': 7, 'grapes': 5}

Sorted by Key: {'apple': 10, 'banana': 3, 'grapes': 5, 'orange': 7}

Sorted by Value: {'banana': 3, 'grapes': 5, 'orange': 7, 'apple': 10}
```

---

## 🔍 Explanation

1. **Sorting by Key**: The dictionary is sorted based on the keys (alphabetical order in this case). We use the `sorted()` function with `dict.items()` and convert the result back to a dictionary.

2. **Sorting by Value**: The dictionary is sorted by the values, which involves using a lambda function to extract the value (`item[1]`) in the sorting process.

3. **Key Points**:
   - `sorted()` returns a sorted list of tuples (key-value pairs).
   - `key=lambda item: item[1]` sorts based on the value (the second element of the tuple).
   - Both sorting methods return a new sorted dictionary.

---

## 🎯 Use Case

Sorting dictionaries is useful in many applications, such as:

- Ranking items by values.
- Organizing data alphabetically or numerically.
- Presenting data in a structured format for better readability.

---
