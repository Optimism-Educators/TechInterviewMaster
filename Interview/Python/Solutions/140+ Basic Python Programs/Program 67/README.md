# Program67
Here is **Program 67** in the requested format:

---

```markdown
# 📝 Program 67: Extract Unique Dictionary Values (Python)

This Python program extracts unique values from a dictionary.

---

## 📌 Problem Statement

**Write a Python program to extract unique dictionary values.**

---

## 💡 What are Dictionary Values?

In Python, a **dictionary** is a collection of key-value pairs. The **values** in a dictionary can be of any data type. This program will extract the unique values from the dictionary.

---

## ✅ Sample Code

```python
# Function to extract unique values from the dictionary
def extract_unique_values(input_dict):
    # Get all the values from the dictionary and convert them into a set
    # A set automatically removes duplicates
    unique_values = set(input_dict.values())
    return unique_values

# Input dictionary from user
input_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
}

# Extract unique values from the dictionary
unique_values = extract_unique_values(input_dict)

# Print the unique values
print("Unique values in the dictionary:", unique_values)
```

---

## ▶️ Example Output

```bash
Unique values in the dictionary: {10, 20, 30}
```

---

## 🔍 Explanation

1. **Values Extraction**: The `.values()` method is used to extract all the values from the dictionary.
2. **Removing Duplicates**: We convert the list of values into a **set**, which automatically removes duplicates and only retains unique values.
3. **Returning Unique Values**: The function returns a set containing only the unique values from the dictionary.

---

📘 This program is useful for finding distinct values from dictionaries, which can be helpful in data cleaning or processing tasks.

```

---

Let me know if you'd like any further clarification or adjustments! 😊
