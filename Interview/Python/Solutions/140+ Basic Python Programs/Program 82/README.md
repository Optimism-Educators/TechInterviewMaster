
# 📘 Program 82: Compute Word Frequency and Sort by Word

This Python program computes the frequency of each word from an input sentence and displays the result in alphanumerical order of the words.

---

## 📌 Problem Statement

**Write a program to compute the frequency of the words from a given input. The output should be sorted alphanumerically by the word (key).**

---

## 🧾 Input Format

- A single sentence or paragraph input from the user.

### Example Input:
```

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

```

---

## ✅ Output Format

- Print each word and its count in the format: `word:count`
- Output is sorted by words (keys) alphabetically.

### Example Output:
```

2:2  
3.:1  
3?:1  
New:1  
Python:5  
Read:1  
and:1  
between:1  
choosing:1  
or:2  
to:1  

```

---

## 🧠 Logic

- Take input as a string.
- Split the string into words.
- Use a dictionary to store and count occurrences.
- Sort the dictionary by key.
- Print each key-value pair.

---

## 🧪 Sample Code

```python
# Take input from the user
text = input("Enter a sentence: ")

# Split into words
words = text.split()

# Create a dictionary to hold frequency
freq = {}

# Count frequency of each word
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Sort and print the dictionary
for word in sorted(freq):
    print(f"{word}:{freq[word]}")
```

---

## 🎯 Example Execution

```bash
Enter a sentence: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2:2  
3.:1  
3?:1  
New:1  
Python:5  
Read:1  
and:1  
between:1  
choosing:1  
or:2  
to:1  
```

---

## 🧠 Notes

- This program doesn't remove punctuation, so `3?`, `3.`, and `3` are treated as different words.
- You can use regex or string punctuation removal for more advanced text processing.

---
