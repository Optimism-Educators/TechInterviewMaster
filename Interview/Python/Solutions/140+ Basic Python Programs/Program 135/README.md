
## 📘 Program 135 – Sort List of Strings by Length

### 📝 Description  

This program defines a function `sort_by_length()` that takes a list of strings and returns the list sorted from the shortest string to the longest string. It ensures that the strings are arranged in increasing order of their lengths.

### ✅ Examples

```python
sort_by_length(["Google", "Apple", "Microsoft"])
# ➞ ["Apple", "Google", "Microsoft"]

sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
# ➞ ["Raphael", "Leonardo", "Donatello", "Michelangelo"]

sort_by_length(["Turing", "Einstein", "Jung"])
# ➞ ["Jung", "Turing", "Einstein"]
```

---

### 🧠 Function Logic

- **sort_by_length(list_of_strings)**:
  - This function takes a list of strings as input.
  - It sorts the strings based on their lengths, from the shortest string to the longest.
  - The sorted list is then returned.

The function uses Python’s built-in sorting mechanism to achieve this efficiently.

---

### 🧠 Function Definition

```python
def sort_by_length(lst):
    return sorted(lst, key=len)
```

---

### 🔁 How to Use

1. Pass a list of strings to the `sort_by_length()` function.
2. The function will return the list sorted by string length, from shortest to longest.

### 💡 Example Usage

```python
# Input list
input_list = ["Google", "Apple", "Microsoft"]

# Call the function
sorted_list = sort_by_length(input_list)

# Output the result
print(sorted_list)   # Output: ["Apple", "Google", "Microsoft"]
```

---

### 🧠 Example Walkthrough

For the input `["Google", "Apple", "Microsoft"]`:

- **"Apple"** has the shortest length (5 characters).
- **"Google"** comes next with 6 characters.
- **"Microsoft"** has the longest length (10 characters).

The sorted list will be: `["Apple", "Google", "Microsoft"]`.

For the input `["Leonardo", "Michelangelo", "Raphael", "Donatello"]`:

- **"Raphael"** (7 characters).
- **"Leonardo"** (8 characters).
- **"Donatello"** (9 characters).
- **"Michelangelo"** (12 characters).

The sorted list will be: `["Raphael", "Leonardo", "Donatello", "Michelangelo"]`.

---

### 🧠 Additional Notes

- The function uses Python’s built-in `sorted()` function with the `key=len` argument to sort the list based on string lengths.
- The input list is assumed to contain strings of varying lengths, and the function will return the sorted list accordingly.

---

### 🔍 Example Input/Output

- **Input**: `["Google", "Apple", "Microsoft"]`
  - **Output**: `["Apple", "Google", "Microsoft"]`

- **Input**: `["Leonardo", "Michelangelo", "Raphael", "Donatello"]`
  - **Output**: `["Raphael", "Leonardo", "Donatello", "Michelangelo"]`

- **Input**: `["Turing", "Einstein", "Jung"]`
  - **Output**: `["Jung", "Turing", "Einstein"]`

