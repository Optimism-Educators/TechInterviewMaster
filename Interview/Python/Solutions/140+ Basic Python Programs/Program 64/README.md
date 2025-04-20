# Program64
Here is **Program 64** in the requested format:

---

```markdown
# 📝 Program 64: Find Uncommon Words from Two Strings (Python)

This Python program finds the **uncommon words** between two strings, meaning it identifies words that are present in **only one of the two strings**.

---

## 📌 Problem Statement

**Write a Python program to find uncommon words from two given strings.**

---

## 💡 What are Uncommon Words?

**Uncommon words** are those words that appear in one string but **not in both**. If a word appears in both strings, it is not considered uncommon.

For example:
- String 1: `"apple orange banana"`
- String 2: `"banana mango grape"`

The **uncommon words** would be: `"apple orange mango grape"`

---

## ✅ Sample Code

```python
# Function to find uncommon words from two strings
def find_uncommon_words(str1, str2):
    # Convert strings to sets of words
    set1 = set(str1.split())
    set2 = set(str2.split())

    # Find the symmetric difference (words that are in one string but not both)
    uncommon_words = set1.symmetric_difference(set2)

    return uncommon_words

# Input from user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find and display uncommon words
uncommon = find_uncommon_words(string1, string2)
print("Uncommon words:", uncommon)
```

---

## ▶️ Example Output

```bash
Enter the first string: apple orange banana
Enter the second string: banana mango grape
Uncommon words: {'grape', 'mango', 'apple', 'orange'}
```

---

## 🔍 Explanation

1. **Splitting**: The strings are split into individual words using `.split()`.
2. **Set operations**: We convert the lists of words into sets and use `symmetric_difference()` to find words that are in either string but not both.

---

📘 This is useful for text comparison and finding unique terms in datasets or documents.

```

---

Let me know if you'd like the next program or any changes! 😊
