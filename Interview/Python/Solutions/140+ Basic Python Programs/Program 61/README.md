# Program61
Absolutely! Here's **Program 61** in your preferred format:

---

```markdown
# 📝 Program 61: Remove the i-th Character from a String (Python)

This Python program removes a character from a specified index `i` in a given string.

---

## 📌 Problem Statement

**Write a Python program to remove the character at position `i` in a string.**

---

## 💡 Understanding the Problem

To remove the character at index `i`:
- Strings are immutable in Python, so we can’t change them directly.
- Instead, we’ll construct a new string by omitting the `i`-th character.

---

## ✅ Sample Code

```python
# Function to remove the i-th character
def remove_char(string, i):
    if i < 0 or i >= len(string):
        return "Index out of range!"
    return string[:i] + string[i+1:]

# User input
input_str = input("Enter a string: ")
index = int(input("Enter the index (i) of the character to remove: "))

# Result
result = remove_char(input_str, index)
print("String after removal:", result)
```

---

## ▶️ Example Output

```bash
Enter a string: pineapple
Enter the index (i) of the character to remove: 4
String after removal: pinepple
```

---

## ⚠️ Notes

- Indexing starts at `0`. So in `"pineapple"`, index 4 corresponds to the second `"a"`.
- Make sure the index `i` is valid (i.e., not less than 0 and less than the length of the string).

---

✂️ This is a handy method when manipulating strings during text processing or data cleaning.

```

---

Let me know if you want **Program 62** next!
