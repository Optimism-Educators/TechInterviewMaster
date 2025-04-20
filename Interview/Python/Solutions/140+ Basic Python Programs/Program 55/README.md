# Program55
Sure! Here's how you'd structure **Program 55** in the same style:

---

```markdown
# 📝 Program 55: Print Even Numbers in a List (Python)

This Python program filters and prints all the even numbers from a list provided by the user.

---

## 📌 Problem Statement

**Write a Python program to print even numbers in a list.**

---

## 🔢 What is the Objective?

The program should take a list of integers and return only those numbers that are **even** (i.e., divisible by 2 with no remainder).

---

## ✅ Sample Code

```python
# Function to return even numbers from a list
def get_even_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers

# Input: List of numbers
input_list = list(map(int, input("Enter numbers separated by space: ").split()))

# Get even numbers
result = get_even_numbers(input_list)

# Output
print("Even numbers in the list are:", result)
```

---

## ▶️ Example Output

```bash
Enter numbers separated by space: 12 5 8 7 10 3 2
Even numbers in the list are: [12, 8, 10, 2]
```

---

## 📁 Suggested Project Structure

```
even_numbers_in_list/
├── even_numbers.py
└── README.md
```

---

## 💡 You Can Try

- Modify the program to **count** how many even numbers are in the list.
- Extend it to **filter both even and odd numbers** and display them separately.
- Add a **GUI** using Tkinter for list input and output display.

---

Happy Coding! 👨‍💻🚀

```

---

Let me know if you'd like the next program in the same format!
