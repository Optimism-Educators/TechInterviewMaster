
# 🔍 Program 86: Binary Search in a Sorted List

This Python program implements a **binary search** function to search for an item in a sorted list. It returns the **index** of the element if found, otherwise `-1`.

---

## 📌 Problem Statement

Write a Python program that implements **binary search**.  
Given a sorted list and an item to search, return the **index** of the element in the list.  
If the element is **not found**, return `-1`.

---

## 🧠 Concepts Used

- Binary Search Algorithm
- Divide and conquer
- Time Complexity: O(log n)

---

## 🧪 Sample Code

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found

# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
```

---

## 🎯 Output (Example)

```
Element 11 found at index 5.
```

---

## ✅ Notes

- The input list **must be sorted** for binary search to work correctly.
- Binary search significantly reduces the time complexity compared to linear search for large datasets.

---
