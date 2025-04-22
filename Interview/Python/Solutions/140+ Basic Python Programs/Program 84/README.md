
# 🗣️ Program 84: Generate All Possible Sentences (Subject + Verb + Object)

This Python program generates all possible sentences by combining subjects, verbs, and objects from given lists.

---

## 📌 Problem Statement

Write a Python program to generate **all sentences** where:

- **Subject** is in: `["I", "You"]`
- **Verb** is in: `["Play", "Love"]`
- **Object** is in: `["Hockey", "Football"]`

Each sentence should be constructed in the form:

```

<Subject> <Verb> <Object>

```

---

## 🧠 Concepts Used

- Nested loops
- String formatting
- List iteration

---

## 🧪 Sample Code

```python
# Lists of subjects, verbs, and objects
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

# Generate and print all possible sentences
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}")
```

---

## 🎯 Output

```
I Play Hockey  
I Play Football  
I Love Hockey  
I Love Football  
You Play Hockey  
You Play Football  
You Love Hockey  
You Love Football
```

---

## 🧠 Notes

- This is a practical use of **combinatorics** in programming.
- You can expand this logic by adding more elements to any of the lists.

---
