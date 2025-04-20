
# 📝 Program 56: Print Odd Numbers in a List (Python)

This Python program filters and prints all the **odd numbers** from a list entered by the user.

---

## 📌 Problem Statement

**Write a Python program to print odd numbers in a list.**

---

## 🔢 What is the Objective?

The program should take a list of integers and return only those numbers that are **odd** (i.e., not divisible by 2).

---

## ✅ Sample Code

```python
# Function to return odd numbers from a list
def get_odd_numbers(num_list):
    odd_numbers = [num for num in num_list if num % 2 != 0]
    return odd_numbers

# Input: List of numbers
input_list = list(map(int, input("Enter numbers separated by space: ").split()))

# Get odd numbers
result = get_odd_numbers(input_list)

# Output
print("Odd numbers in the list are:", result)
```

---

## ▶️ Example Output

```bash
Enter numbers separated by space: 11 4 9 2 7 8 1
Odd numbers in the list are: [11, 9, 7, 1]
```

---

## 📁 Suggested Project Structure

```
odd_numbers_in_list/
├── odd_numbers.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to **count** how many odd numbers are in the list.
- Extend it to **display both odd and even numbers**.
- Add input **validation** to reject non-integer values.

---
