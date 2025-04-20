# Program102
Sure! Here's **Program 102** in the same format as your previous requests:

---

```markdown
# 🟩 Program 102: Filter Strings from a List

This Python program filters out all string elements from a list containing both integers and strings.

---

## 📌 Problem Statement

Create a function that takes a list of **non-negative integers and strings**, and returns a new list that contains **only the integers**.

---

## 🧪 Examples

### Input:
```python
filter_list([1, 2, "a", "b"])
filter_list([1, "a", "b", 0, 15])
filter_list([1, 2, "aasf", "1", "123", 123])
```

### Output

```
[1, 2]
[1, 0, 15]
[1, 2, 123]
```

---

## 🧠 Concepts Used

- Type checking using `isinstance()`
- List comprehension

---

## ✅ Constraints

- The list may include integers and strings only.
- The output list must contain only integers.

---

## 🧪 Sample Code

```python
def filter_list(lst):
    return [item for item in lst if isinstance(item, int)]

# Test cases
print(filter_list([1, 2, "a", "b"]))                 # ➞ [1, 2]
print(filter_list([1, "a", "b", 0, 15]))             # ➞ [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # ➞ [1, 2, 123]
```

---

## 🎯 Output Explanation

- `"a"`, `"b"` are removed → `[1, 2]`
- Only integers `1`, `0`, `15` kept → `[1, 0, 15]`
- Strings `"aasf"`, `"1"`, `"123"` are removed → `[1, 2, 123]`

---

✅ This is a clean and efficient way to filter data types from a mixed list.

```
