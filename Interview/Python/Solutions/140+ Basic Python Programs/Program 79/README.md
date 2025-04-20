# Program79
Here is **Program 79** in your preferred format:

---

```markdown
# 📝 Program 79: Count Letters and Digits in a Sentence

This Python program accepts a sentence as input and calculates the number of **alphabetic letters** and **numeric digits** in it.

---

## 📌 Problem Statement

**Write a Python program that accepts a sentence and calculates the number of letters and digits in it.**

### Example

Suppose the following input is supplied to the program:

```

hello world! 123

```

Then the output should be:

```

LETTERS 10  
DIGITS 3

```

---

## 💡 Explanation

1. **Input**:
   - The user is asked to enter a sentence.
   
2. **Logic**:
   - Loop through each character in the input.
   - Use `isalpha()` to check if a character is a letter.
   - Use `isdigit()` to check if a character is a digit.
   - Maintain counters for both letters and digits.
   
3. **Output**:
   - Display the count of letters and digits found in the input.

---

## ✅ Sample Code

```python
# Initialize counters
letters = 0
digits = 0

# Input a sentence
sentence = input("Enter a sentence: ")

# Iterate over each character in the input
for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# Print the results
print(f"LETTERS {letters}")
print(f"DIGITS {digits}")
```

---

## ▶️ Example Output

```bash
Enter a sentence: hello world! 123
LETTERS 10
DIGITS 3
```

---

## 🔍 Breakdown

- `"hello world"` contains 10 alphabetic letters.
- `"123"` contains 3 digits.
- Punctuation (`!`) and spaces are ignored for this count.

---

## 🎯 Use Case

Useful in scenarios like text analysis, form validation, or content moderation where understanding the composition of a string is required.

---
