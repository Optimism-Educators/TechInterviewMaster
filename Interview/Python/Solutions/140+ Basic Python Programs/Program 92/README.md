
# 🟩 Program 92: Stuttering a Word

This Python program defines a function `stutter()` that takes a word as input and simulates the stuttering effect of someone struggling to read the word. The first two letters of the word are repeated twice, followed by an ellipsis ("...") and a space. The word is then pronounced with a question mark ("?").

---

## 📌 Problem Statement

Write a function `stutter()` that takes a word as input and returns a stuttered version of the word, where the first two letters are repeated twice, followed by an ellipsis, and then the full word with a question mark at the end.

---

## 🧠 Concepts Used

- String Manipulation
- Function Definition
- String Concatenation

---

## 🧪 Sample Code

```python
def stutter(word):
    # Repeat the first two characters twice, then the full word with a question mark
    return f"{word[:2]}... {word[:2]}... {word}?"

# Test cases
print(stutter("incredible"))  # Output: in... in... incredible?
print(stutter("enthusiastic"))  # Output: en... en... enthusiastic?
print(stutter("outstanding"))  # Output: ou... ou... outstanding?
```

---

## 🎯 Example Input & Output

### Input

```
"incredible"
"enthusiastic"
"outstanding"
```

### Output

```
in... in... incredible?
en... en... enthusiastic?
ou... ou... outstanding?
```

---

## ✅ Notes

- The function assumes all input is in lowercase and contains at least two characters, as per the problem's hint.
- The function uses string slicing to grab the first two characters and constructs the stuttered version of the word by repeating them.

---
