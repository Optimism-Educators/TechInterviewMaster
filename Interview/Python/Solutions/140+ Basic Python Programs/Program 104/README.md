
# 🟩 Program 104: Destructuring Assignment in Python

This Python program demonstrates how to **unpack** elements from a list into variables using **destructuring assignment**.

---

## 📌 Problem Statement

Given a list of numbers, extract:

- `first` → The first element  
- `middle` → A list of all elements between first and last  
- `last` → The last element

---

## 🧪 Example

```python
lst = [1, 2, 3, 4, 5, 6]
```

### Expected Output

```
first ➞ 1
middle ➞ [2, 3, 4, 5]
last ➞ 6
```

---

## 🧠 Concept Used

- List slicing
- Destructuring (unpacking) values from a list

---

## 🧪 Sample Code

```python
lst = [1, 2, 3, 4, 5, 6]

# Destructuring assignment
first, *middle, last = lst

# Output the values
print("First:", first)
print("Middle:", middle)
print("Last:", last)
```

---

## 💡 Output

```
First: 1
Middle: [2, 3, 4, 5]
Last: 6
```

---
