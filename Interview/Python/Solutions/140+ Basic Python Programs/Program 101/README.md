# Program101
Here’s **Program 101** written in your requested style:

---

```markdown
# 🟩 Program 101: Hamming Distance Between Two Strings

This Python program calculates the Hamming distance between two strings of equal length.

---

## 📌 Problem Statement

The **Hamming distance** is defined as the number of positions at which the corresponding characters of two strings are different.

🧠 **Formula**: Compare each character in the same position in both strings and count how many are different.

---

## 🧪 Examples

### Input:
```python
hamming_distance("abcde", "bcdef")
hamming_distance("abcde", "abcde")
hamming_distance("strong", "strung")
```

### Output

```
5
0
1
```

---

## 🧠 Concepts Used

- String traversal
- Character comparison
- Length checking

---

## ✅ Conditions

- Both strings must be of the same length.
- If not, an error or validation should be handled.

---

## 🧪 Sample Code

```python
def hamming_distance(s1, s2):
    # Check if both strings have equal length
    if len(s1) != len(s2):
        return "Strings must be of equal length."

    # Count the differences
    distance = sum(char1 != char2 for char1, char2 in zip(s1, s2))
    return distance

# Test cases
print(hamming_distance("abcde", "bcdef"))   # Output: 5
print(hamming_distance("abcde", "abcde"))   # Output: 0
print(hamming_distance("strong", "strung")) # Output: 1
```

---

## 🎯 Output Explanation

- `"abcde"` vs `"bcdef"` → All characters differ → Output: `5`
- `"abcde"` vs `"abcde"` → All characters same → Output: `0`
- `"strong"` vs `"strung"` → Only 1 character differs (`o` vs `u`) → Output: `1`

---

## 📘 Note

If you pass strings of different lengths, the function will return an error message:

```python
print(hamming_distance("short", "longer"))
# Output: "Strings must be of equal length."
```

---

Let me know if you'd like a version that automatically handles different string lengths or ignores case! ✅

```
