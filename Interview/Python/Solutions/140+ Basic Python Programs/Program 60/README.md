
# 📝 Program 60: Find Words Greater Than a Given Length k (Python)

This Python program helps you find all the **words in a sentence that are longer than a given length**.

---

## 📌 Problem Statement

**Write a Python program to find all words in a string that are greater than a given length `k`.**

---

## 💡 Understanding the Problem

We’ll:
- Take a string input from the user.
- Split it into individual words.
- Compare the length of each word with `k`.
- Print all words with length greater than `k`.

---

## ✅ Sample Code

```python
# Function to filter words greater than length k
def long_words(string, k):
    words = string.split()  # split sentence into words
    result = [word for word in words if len(word) > k]
    return result

# User input
input_string = input("Enter a sentence: ")
k = int(input("Enter the minimum length k: "))

# Get words greater than k
output = long_words(input_string, k)

# Display result
print(f"Words longer than {k} characters are:", output)
```

---

## ▶️ Example Output

```bash
Enter a sentence: Python is a powerful and versatile programming language
Enter the minimum length k: 6
Words longer than 6 characters are: ['powerful', 'versatile', 'programming', 'language']
```

---

## 🧠 Note

- You can adjust the condition in the list comprehension to get words equal to or less than `k` if needed.
- Use `string.lower().split()` if you want case-insensitive processing.

---

