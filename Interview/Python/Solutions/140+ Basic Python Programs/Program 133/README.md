# Program133
Here is the **README.md** file for **Program 133 – Find the Unique Number**:

---

## 📘 Program 133 – Find the Unique Number

### 📝 Description  

This program defines a function `unique()` that takes a list of numbers and returns the number that is unique in the list. All the other numbers in the list will be identical, except for one number, which is different. The function will find and return that unique number.

### 🔍 Purpose  

The function helps in identifying a unique number in a list where the majority of the numbers are identical. This is particularly useful in scenarios where you want to isolate or detect an outlier number in a dataset.

---

### ✅ Examples

```python
unique([3, 3, 3, 7, 3, 3]) ➞ 7

unique([0, 0, 0.77, 0, 0]) ➞ 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
```

---

### 💡 Function Logic

1. **Input**: The function takes a list of numbers, where one number is unique and the others are identical.
2. **Process**:
   - Iterate through the list of numbers.
   - Check for the unique number in the list.
3. **Return**: The function returns the unique number found in the list.

---

### 🧠 Function Definition

```python
def unique(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
```

---

### 🔁 How to Use

1. Call the `unique()` function with a list of numbers.
2. The function will return the unique number that is different from the others in the list.

### 💡 Example Usage

```python
result = unique([3, 3, 3, 7, 3, 3])
print(result)  # Output: 7
```

---

### 🧠 Example Walkthrough

For the input `[3, 3, 3, 7, 3, 3]`:

- The function iterates through the list and checks the count of each number.
- `7` appears only once, while `3` appears multiple times.
- The function identifies `7` as the unique number and returns it.

For the input `[0, 0, 0.77, 0, 0]`:

- The function identifies `0.77` as the unique number and returns it.

For the input `[0, 1, 1, 1, 1, 1, 1, 1]`:

- The function identifies `0` as the unique number and returns it.

---

### 🧠 Additional Notes

- The function assumes that the input list will always have exactly one unique number while all others are the same.
- The function handles both integer and floating-point numbers.

---

### 🔍 Example Input/Output

- **Input**: `[3, 3, 3, 7, 3, 3]`
  - **Output**: `7`
  
- **Input**: `[0, 0, 0.77, 0, 0]`
  - **Output**: `0.77`
  
- **Input**: `[0, 1, 1, 1, 1, 1, 1, 1]`
  - **Output**: `0`
