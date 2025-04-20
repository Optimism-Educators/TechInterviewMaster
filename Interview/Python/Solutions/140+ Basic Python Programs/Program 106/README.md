
## 🧮 Program 106: Move All Elements of One Type to End of List

### 📌 Description

This Python function, `move_to_end(lst, element)`, moves **all occurrences of a specific element** to the **end of a given list**, while preserving the order of the other elements.

### ✅ Function Signature

```python
def move_to_end(lst, element):
```

### 🔧 Parameters

- `lst` *(list)*: A list containing elements of any type (integers, strings, etc.).
- `element` *(any)*: The specific element to be moved to the end of the list.

### 📤 Returns

- A new list with all occurrences of the specified element moved to the end.

---

### 💡 Example Usage

```python
print(move_to_end([1, 3, 2, 4, 4, 1], 1))
# ➞ [3, 2, 4, 4, 1, 1]

print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
# ➞ [7, 8, 1, 2, 3, 4, 9]

print(move_to_end(["a", "a", "a", "b"], "a"))
# ➞ ["b", "a", "a", "a"]
```

---

### 🧠 How It Works

- The function separates the elements **not equal** to the target into one list.
- It then adds all instances **equal** to the target element at the end.

---

### 🛠️ Full Code

```python
def move_to_end(lst, element):
    # Filter out elements not equal to the target
    others = [x for x in lst if x != element]
    
    # Count and add the target element at the end
    targets = [x for x in lst if x == element]
    
    return others + targets
```

---
