# Program113
Sure! Here's **Program 113** in the same format:

---

## 📘 Program 113 - Add Index to List Elements

### 🔍 Description  

Create a function that takes a list of numbers and returns a new list where each element is increased by its index in the list.  
For example, add 0 to the number at index 0, add 1 to the number at index 1, and so on.

---

### 🧠 Function Signature

```python
def add_indexes(lst):
```

---

### 🧮 Parameters  

- `lst` (List[int]): A list of integers.

---

### 🚀 Returns  

- `List[int]`: A new list where each element is the sum of the original value and its index.

---

### ✅ Examples

```python
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]  
add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]  
add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
```

---

### 🧪 Sample Code

```python
def add_indexes(lst):
    return [num + idx for idx, num in enumerate(lst)]

# Example usage
print(add_indexes([0, 0, 0, 0, 0]))  # ➞ [0, 1, 2, 3, 4]
print(add_indexes([1, 2, 3, 4, 5]))  # ➞ [1, 3, 5, 7, 9]
print(add_indexes([5, 4, 3, 2, 1]))  # ➞ [5, 5, 5, 5, 5]
```

---

### 📌 Notes

- This program uses `enumerate()` to access both the **index** and **value** of each element.
- Clean and efficient solution using **list comprehension**.

---

Let me know if you want a README version or want this compiled into a document or notebook!
