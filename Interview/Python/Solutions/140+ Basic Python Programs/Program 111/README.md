
## 📘 Program 111 - Find Even Numbers Using List Comprehension

### 🔍 Description  

This Python function uses list comprehension to find and return all even numbers from 1 up to a given number `n` (inclusive).

---

### 🧠 Function Signature

```python
def find_even_nums(n):
```

---

### 🧮 Parameters  

- `n` (int): A positive integer indicating the upper limit of the range (inclusive).

---

### 🚀 Returns  

- `List[int]`: A list containing all even numbers from 1 to `n`.

---

### ✅ Examples

```python
find_even_nums(8) ➞ [2, 4, 6, 8]  
find_even_nums(4) ➞ [2, 4]  
find_even_nums(2) ➞ [2]
```

---

### 🧪 Sample Code

```python
def find_even_nums(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

# Example usage
print(find_even_nums(8))  # Output: [2, 4, 6, 8]
print(find_even_nums(4))  # Output: [2, 4]
print(find_even_nums(2))  # Output: [2]
```

---

### 📌 Notes

- This program is a concise and Pythonic way to generate even numbers using list comprehensions.
- Ensure `n` is greater than or equal to 1 to avoid returning an empty list.
