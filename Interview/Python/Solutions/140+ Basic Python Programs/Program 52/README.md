
# 📝 Program 52: Find the Largest Number in a List (Python)

This Python program finds the largest number in a given list.

---

## 📌 Problem Statement

**Write a Python program to find the largest number in a list.**

---

## 🔢 What is the Objective?

The program should take a list of numbers and identify the largest (maximum) number in the list. If the list is empty, the program should handle that scenario appropriately (e.g., by displaying a message indicating the list is empty).

---

## ✅ Sample Code

```python
# Python program to find the largest number in a list

# Function to find the largest number in the list
def find_largest_number(numbers):
    if not numbers:  # Check if the list is empty
        return "List is empty"
    
    # Initialize the largest number as the first element
    largest = numbers[0]
    
    # Loop through the list to find the largest number
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if a larger number is found
    
    return largest

# Example list
numbers = [12, 45, 67, 2, 89, 4]

# Calling the function and printing the result
largest_number = find_largest_number(numbers)
print(f"The largest number in the list is: {largest_number}")
```

---

## ▶️ Example Output

```bash
The largest number in the list is: 89
```

---

## 📁 Suggested Project Structure

```
find_largest_number/
├── find_largest_number.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to handle lists containing **negative numbers** or **floating-point numbers**.
- Test the program with **duplicates** or an empty list to see how it behaves.
- You could also implement this using Python's built-in `max()` function for a more concise solution.

---
