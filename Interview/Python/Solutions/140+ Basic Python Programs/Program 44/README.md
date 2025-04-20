# Program44
Here's a structured explanation and code for **Program 44: Print All Disarium Numbers Between 1 and 100**:

---

```markdown
# 📝 Program 44: Print All Disarium Numbers Between 1 and 100 (Python)

This Python program prints all **Disarium numbers** between 1 and 100. A **Disarium number** is a number where the sum of its digits, each raised to the power of its respective position, equals the number itself.

---

## 📌 Problem Statement

**Write a Python program to print all Disarium numbers between 1 and 100.**

---

## 🔢 Explanation

A **Disarium number** is defined as a number where:
\[
\text{sum of digits raised to their respective positions} = \text{the number itself}.
\]

For example:
- **89** is a Disarium number because:
  \[
  8^1 + 9^2 = 8 + 81 = 89
  \]

### Steps:
1. Loop through numbers from 1 to 100.
2. For each number, calculate the sum of its digits raised to the power of their respective positions.
3. Print the number if it matches the Disarium condition.

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

# Print all Disarium numbers between 1 and 100
print("Disarium numbers between 1 and 100 are:")
for num in range(1, 101):
    if is_disarium_number(num):
        print(num, end=" ")
```

---

## ▶️ Example Output

```bash
Disarium numbers between 1 and 100 are:
1 2 3 4 5 6 7 8 9 89
```

---

## 📁 Suggested Project Structure

```
disarium_numbers/
├── disarium_numbers.py
└── README.md
```

---

## 💡 You Can Try

- Extend the program to find Disarium numbers in a larger range (e.g., up to 1000).
- Modify the program to display the powers for each digit that contributes to the Disarium number.

---

Happy Coding! 🚀

```

This program prints all the Disarium numbers between 1 and 100 by checking each number in the range using the `is_disarium_number()` function. Let me know if you need further explanations or enhancements!
