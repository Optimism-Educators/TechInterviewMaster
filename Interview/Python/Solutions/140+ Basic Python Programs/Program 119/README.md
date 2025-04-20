
## 📘 Program 119 – Alphabetical Order of Letters

### 📝 Description  

This program defines a function `alphabet_soup(s)` that takes a string as input and returns the string with its letters sorted in alphabetical order. The function sorts the characters in ascending order and returns the rearranged string.

---

### ✅ Examples

```python
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"
```

---

### 💡 Function Logic

- Convert the input string into a list of characters.
- Sort the list in alphabetical order.
- Join the sorted list of characters back into a string.
- Return the sorted string.

---

### 🧠 Function Definition

```python
def alphabet_soup(s):
    return ''.join(sorted(s))
```

---

### 🔁 How to Use

1. Provide a string of letters to the `alphabet_soup()` function.
2. The function sorts the characters of the string in alphabetical order.
3. The function returns the sorted string.

