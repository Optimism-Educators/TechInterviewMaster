
# 📝 Program 53: Find the Second Largest Number in a List (Python)

This Python program finds the second largest number in a given list.

---

## 📌 Problem Statement

**Write a Python program to find the second largest number in a list.**

---

## 🔢 What is the Objective?

The program should take a list of numbers and identify the second largest number. If the list contains fewer than two elements, the program should handle that scenario by displaying an appropriate message indicating that finding the second largest number is not possible.

---

## ✅ Sample Code

```python
# Python program to find the second largest number in a list

# Function to find the second largest number in the list
def find_second_largest(numbers):
    if len(numbers) < 2:  # Check if the list has fewer than 2 elements
        return "List must contain at least two numbers."
    
    # Remove duplicates by converting the list to a set and then back to a list
    numbers = list(set(numbers))
    
    # If there is only one unique number, there's no second largest
    if len(numbers) < 2:
        return "No second largest number, all numbers are the same."
    
    # Sort the list and get the second largest
    numbers.sort()
    return numbers[-2]

# Example list
numbers = [12, 45, 67, 89, 67, 2, 45]

# Calling the function and printing the result
second_largest_number = find_second_largest(numbers)
print(f"The second largest number in the list is: {second_largest_number}")
```

---

## ▶️ Example Output

```bash
The second largest number in the list is: 67
```

---

## 📁 Suggested Project Structure

```
find_second_largest_number/
├── find_second_largest_number.py
└── README.md
```

---

## 💡 You Can Try

- Test the program with **lists containing negative numbers** or **floating-point numbers**.
- Handle the case where all the numbers in the list are the same or the list contains only one unique number.
- Try different edge cases, like a **list with only two elements** or a **list with more than two large numbers**.

---
