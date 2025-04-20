Here’s **Program 99** written in the format you requested:

---

```markdown
# 🟩 Program 99: Replace All Vowels in a String

This Python program replaces all the vowels in a string with a specified character.

---

## 📌 Problem Statement

Create a function that takes a string and a specified character, then replaces all vowels in the string (both lowercase and uppercase vowels) with the given character.

### Examples:

- For the input `"the aardvark"` and character `"#"`, the function should return `"th# ##rdv#rk"`.
- For the input `"minnie mouse"` and character `"?"`, the function should return `"m?nn?? m??s?"`.
- For the input `"shakespeare"` and character `"*"`, the function should return `"shkspr*"`.
  
---

## 🧠 Concepts Used

- String manipulation
- Iterating through the string
- Conditional replacement

---

## 🧪 Sample Code

```python
def replace_vowels(string, char):
    vowels = "aeiouAEIOU"
    return ''.join([char if c in vowels else c for c in string])

# Test cases
print(replace_vowels("the aardvark", "#"))        # Output: "th# ##rdv#rk"
print(replace_vowels("minnie mouse", "?"))        # Output: "m?nn?? m??s?"
print(replace_vowels("shakespeare", "*"))         # Output: "shkspr*"
```

---

## 🎯 Example Input & Output

### Input

```
"the aardvark", "#"
"minnie mouse", "?"
"shakespeare", "*"
```

### Output

```
"th# ##rdv#rk"
"m?nn?? m??s?"
"shkspr*"
```

---

## ✅ Notes

- This solution checks each character in the string to see if it is a vowel.
- The function uses `join()` to efficiently create a new string after replacing the vowels.
- Both lowercase and uppercase vowels are considered for replacement.

---

Let me know if you'd like any further modifications! ✨

```
 