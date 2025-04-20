# Program35
Sure! Here's a well-structured explanation and Python program for:

---

```markdown
# 🔀 Program 35: Split the Array and Add the First Part to the End

This program demonstrates how to **split an array** (list) at a specific position and then **move the first part to the end** of the array.

---

## 📌 Problem Statement

**Write a Python program to split an array and add the first part to the end.**

---

## 🔄 What Does It Mean?

Given an array and a position `k`, the task is to:
- Split the array at position `k`
- Move the first part `[0:k]` to the **end** of the array

### Example:

For the array:
```python
[1, 2, 3, 4, 5, 6]
```

If we split at position `2`:

- First part: `[1, 2]`
- Second part: `[3, 4, 5, 6]`

Final result:

```python
[3, 4, 5, 6, 1, 2]
```

---

## ✅ Sample Code

```python
# Python program to split an array and move the first part to the end

def split_and_append(arr, k):
    n = len(arr)
    # Ensure k is within the array length
    k = k % n
    return arr[k:] + arr[:k]

# Input from user
arr = list(map(int, input("Enter the list elements separated by space: ").split()))
k = int(input("Enter the position to split the array: "))

# Result after split and rearrange
result = split_and_append(arr, k)
print("Array after splitting and appending:", result)
```

---

## ▶️ Example Output

```bash
Enter the list elements separated by space: 10 20 30 40 50
Enter the position to split the array: 3
Array after splitting and appending: [40, 50, 10, 20, 30]
```

---

## 📁 Suggested Folder Structure

```
array_split_rearrange/
├── split_append.py
└── README.md
```

---

## 💡 Try This

- Allow the user to choose between **left split** or **right split**.
- Create a function that supports **rotation direction**.
- Extend to **2D matrix** splitting.

---

Happy Coding! 🔧📦

```

Let me know if you'd like this and other programs bundled into a printable format or GitHub repo!
