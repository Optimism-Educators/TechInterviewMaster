# Program138
Here is the **README.md** file for **Program 138 – Dictionary to List Conversion**:

---

## 📘 Program 138 – Dictionary to List Conversion

### 📝 Description  

This program defines a function `dict_to_list()` that converts a dictionary into a list of tuples, where each tuple contains a key-value pair from the dictionary. The resulting list will have the tuples sorted in alphabetical order of the keys.

### ✅ Examples

```python
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
})
# ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
})
# ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
```

---

### 🧠 Function Logic

- **dict_to_list(dictionary)**:
  - The function takes a dictionary as input.
  - It converts the dictionary into a list of tuples where each tuple contains a key and its associated value.
  - The list is sorted in alphabetical order of the keys.

---

### 🧠 Function Definition

```python
def dict_to_list(dictionary):
    # Convert the dictionary to a sorted list of tuples
    return sorted(dictionary.items())
```

---

### 🔁 How to Use

1. Pass a dictionary to the `dict_to_list()` function.
2. The function will convert the dictionary into a list of key-value pairs as tuples and sort them by key.

### 💡 Example Usage

```python
# Input dictionary
my_dict = {"B": 2, "A": 1, "C": 3}

# Call the function
result = dict_to_list(my_dict)

# Output the result
print(result)  # Output: [('A', 1), ('B', 2), ('C', 3)]
```

---

### 🧠 Example Walkthrough

For the input `{"D": 1, "B": 2, "C": 3}`:

- The dictionary will be converted to the list `[("B", 2), ("C", 3), ("D", 1)]` after sorting by keys.

For the input `{"likes": 2, "dislikes": 3, "followers": 10}`:

- The dictionary will be converted to the list `[("dislikes", 3), ("followers", 10), ("likes", 2)]` after sorting by keys.

---

### 🧠 Additional Notes

- The function uses Python's built-in `sorted()` function to sort the dictionary by keys.
- The `items()` method is used to extract key-value pairs from the dictionary.

---

### 🔍 Example Input/Output

- **Input**: `{"D": 1, "B": 2, "C": 3}`
  - **Output**: `[("B", 2), ("C", 3), ("D", 1)]`

- **Input**: `{"likes": 2, "dislikes": 3, "followers": 10}`
  - **Output**: `[("dislikes", 3), ("followers", 10), ("likes", 2)]`
