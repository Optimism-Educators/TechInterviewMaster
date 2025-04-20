# Program72
Here is **Program 72** in the requested format:

---

```markdown
# 📝 Program 72: Check Order of Characters in String Using OrderedDict (Python)

This Python program demonstrates how to check the order of characters in a string using the `OrderedDict()` class. By leveraging `OrderedDict`, we can preserve the order of the characters and compare their positions.

---

## 📌 Problem Statement

**Write a Python program to check the order of characters in a string using `OrderedDict()` class.**

---

## 💡 What is an OrderedDict?

An `OrderedDict` is a subclass of the dictionary that remembers the order of elements based on their insertion order. This property makes it very useful when you need to preserve the order in which items are added.

---

## ✅ Sample Code

```python
from collections import OrderedDict

# Function to check order of characters
def check_order_of_characters(input_string):
    # Create an OrderedDict from the string to preserve order
    ordered_dict = OrderedDict.fromkeys(input_string)
    
    # Print the OrderedDict
    print("OrderedDict with characters:", ordered_dict)

# Test the function
input_string = "programming"
check_order_of_characters(input_string)
```

---

## ▶️ Example Output

```bash
OrderedDict with characters: OrderedDict([('p', None), ('r', None), ('o', None), ('g', None), ('a', None), ('m', None), ('i', None), ('n', None)])
```

---

## 🔍 Explanation

1. **`OrderedDict.fromkeys()`**: This method creates an `OrderedDict` where each character of the string is a key, and the value for each key is set to `None`. The order of insertion is preserved.
2. **Printing the OrderedDict**: The order of characters in the string is printed as an `OrderedDict`. The unique characters are listed in the order in which they first appear in the string.

---

## 🎯 Use Case

This program is helpful when you want to keep track of the order of characters in a string while removing any duplicates. It can be useful for checking patterns or ensuring character sequences in data processing tasks.

---

Let me know if you need any further modifications or explanations! 😊

```

---

I hope this is what you were looking for! Feel free to ask if you need anything else.
