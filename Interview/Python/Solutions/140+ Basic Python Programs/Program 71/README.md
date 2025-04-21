
# 📝 Program 71: Insertion at the Beginning in OrderedDict (Python)

This Python program demonstrates how to insert an item at the beginning of an `OrderedDict`. An `OrderedDict` is a dictionary subclass that maintains the order of elements based on their insertion order.

---

## 📌 Problem Statement

**Write a Python program to insert an item at the beginning of an `OrderedDict`.**

---

## 💡 What is an OrderedDict?

An `OrderedDict` is a dictionary that remembers the order in which items were inserted. Unlike a regular dictionary (which doesn't guarantee any specific order of elements), the `OrderedDict` ensures that items are iterated in the order they were added.

---

## ✅ Sample Code

```python
from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Print the original OrderedDict
print("Original OrderedDict:", ordered_dict)

# Inserting an item at the beginning
ordered_dict.update({'z': 0})  # Adding to the end temporarily
ordered_dict.move_to_end('z', last=False)  # Move 'z' to the beginning

# Print the updated OrderedDict
print("OrderedDict after insertion at the beginning:", ordered_dict)
```

---

## ▶️ Example Output

```bash
Original OrderedDict: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
OrderedDict after insertion at the beginning: OrderedDict([('z', 0), ('a', 1), ('b', 2), ('c', 3)])
```

---

## 🔍 Explanation

1. **`OrderedDict()`**: We create an `OrderedDict` using a list of key-value pairs. The order of the items is preserved.
2. **Inserting an Item**: To insert an item at the beginning, we temporarily add the item to the end of the dictionary using the `update()` method, and then use the `move_to_end()` method to move it to the beginning. By passing `last=False`, we indicate that the item should be moved to the beginning.
3. **Result**: The result is an `OrderedDict` with the new item inserted at the beginning, while the other items maintain their original order.

---
