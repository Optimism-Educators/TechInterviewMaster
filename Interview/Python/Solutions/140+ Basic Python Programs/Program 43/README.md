# Program43
Here's a structured explanation and code for **Program 43: Check if a Number is a Disarium Number**:

---

```markdown
# 📝 Program 43: Check if the Given Number is a Disarium Number (Python)

This Python program checks if a given number is a **Disarium Number**. A **Disarium number** is a number where the sum of its digits, each raised to the power of its respective position, equals the number itself.

---

## 📌 Problem Statement

**Write a Python program to check if the given number is a Disarium number.**

---

## 🔢 Explanation

A Disarium number is a number where the sum of its digits raised to the power of their respective positions equals the number itself.

For example:
- **89** is a Disarium number because:
  \[
  8^1 + 9^2 = 8 + 81 = 89
  \]

### Steps:
1. Convert the number into a string to access each digit.
2. For each digit, raise it to the power of its position (starting from 1).
3. Sum the results and compare the sum to the original number.

---

## ✅ Sample Code

```python
# Function to check if a number is Disarium
def is_disarium_number(num):
    # Convert number to string to easily access each digit
    num_str = str(num)
    length = len(num_str)
    total = 0
    
    # Sum the digits raised to their respective position powers
    for i in range(length):
        total += int(num_str[i]) ** (i + 1)
    
    # Check if the sum equals the original number
    return total == num

# Input number from the user
number = int(input("Enter a number: "))

# Check if the number is a Disarium number
if is_disarium_number(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")
```

---

## ▶️ Example Output

```bash
Enter a number: 89
89 is a Disarium number.

Enter a number: 123
123 is not a Disarium number.
```

---

## 📁 Suggested Project Structure

```
disarium_number/
├── disarium_number.py
└── README.md
```

---

## 💡 You Can Try

- Check for other **special numbers** like Armstrong numbers, Palindrome numbers, etc.
- Implement a version that checks if a range of numbers contains Disarium numbers.

---

Happy Coding! 🚀

```

This program checks whether the entered number is a Disarium number by calculating the sum of each digit raised to the power of its position and comparing it with the original number. Let me know if you'd like more details or examples!
