
## 📘 Program 112 - Filter Integers from a Mixed List

### 🔍 Description  

Create a function that takes a list of mixed data types (strings and integers) and filters it to return a list containing **only integers**.

---

### 🧠 Function Signature

```python
def filter_list(lst):
```

---

### 🧮 Parameters  

- `lst` (List[Union[int, str]]): A list containing integers and strings.

---

### 🚀 Returns  

- `List[int]`: A new list that contains only the integers from the input list.

---

### ✅ Examples

```python
filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]  
filter_list(["A", 0, "Edabit", 1729, "Python", 1729]) ➞ [0, 1729]  
filter_list(["Nothing", "here"]) ➞ []
```

---

### 🧪 Sample Code

```python
def filter_list(lst):
    return [x for x in lst if type(x) == int]

# Example usage
print(filter_list([1, 2, 3, "a", "b", 4]))             # Output: [1, 2, 3, 4]
print(filter_list(["A", 0, "Edabit", 1729, "Python", 1729]))  # Output: [0, 1729]
print(filter_list(["Nothing", "here"]))               # Output: []
```

---

### 📌 Notes

- This program uses **list comprehension** for a clean and efficient solution.
- It strictly checks for `int` type using `type(x) == int`.
