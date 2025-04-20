# Program40
Here's a well-structured explanation and code for:

---

```markdown
# 📝 Program 40: Sort Words in Alphabetic Order (Python)

This Python program sorts a list of words in **alphabetical order**.

---

## 📌 Problem Statement

**Write a Python program to sort words in alphabetic order.**

---

## 🔢 Explanation

Sorting words in **alphabetic order** means arranging them in a sequence from **A to Z**. For instance, sorting a list of words like `["banana", "apple", "cherry"]` results in `["apple", "banana", "cherry"]`.

The sorting is typically done using Python's built-in `sorted()` function or the `sort()` method.

---

## ✅ Sample Code

```python
# Function to sort words in alphabetical order
def sort_words(words):
    return sorted(words)

# Example list of words
words_list = ["banana", "apple", "cherry", "date", "elderberry"]

# Sort words
sorted_words = sort_words(words_list)

# Display sorted words
print("Sorted words in alphabetical order:")
for word in sorted_words:
    print(word)
```

---

## ▶️ Example Output

```bash
Sorted words in alphabetical order:
apple
banana
cherry
date
elderberry
```

---

## 📁 Suggested Project Structure

```
alphabetical_sort/
├── sort_words.py
└── README.md
```

---

## 💡 You Can Try

- **Sort words in reverse alphabetical order** using `sorted(words, reverse=True)`.
- **Sort words case-insensitively** by using `sorted(words, key=str.lower)`.

---
