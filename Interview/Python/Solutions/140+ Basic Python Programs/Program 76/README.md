# Program76
Here is **Program 76** in the requested format:

---

```markdown
# 📝 Program 76: Sort Words Alphabetically in a Comma-Separated Sequence

This Python program accepts a comma-separated sequence of words as input and then prints the words in a comma-separated sequence after sorting them alphabetically.

---

## 📌 Problem Statement

**Write a Python program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.**

### Example

Suppose the following input is supplied to the program:
- Input: `without,hello,bag,world`

Then, the output of the program should be:
```

bag,hello,without,world

```

---

## 💡 Explanation

1. **Input**:
   - The user is asked to input a sequence of words, separated by commas.
   
2. **Logic**:
   - The input string is split into a list of words.
   - The list is then sorted alphabetically.
   - The sorted list is joined back into a single string, with each word separated by a comma.
   
3. **Output**:
   - A string of words is printed in alphabetical order, separated by commas.

---

## ✅ Sample Code

```python
# Function to sort and print words in a comma-separated sequence
def sort_words(words):
    word_list = words.split(',')  # Split input string into list of words
    word_list.sort()  # Sort the list alphabetically
    sorted_words = ','.join(word_list)  # Join the list into a comma-separated string
    return sorted_words

# Input the comma-separated sequence of words
words = input("Enter words separated by commas: ")

# Get the sorted words
sorted_result = sort_words(words)

# Print the result
print(sorted_result)
```

---

## ▶️ Example Output

```bash
Enter words separated by commas: without,hello,bag,world
bag,hello,without,world
```

---

## 🔍 Explanation

1. **Input**:
   - The user is prompted to input a sequence of words, separated by commas (e.g., `without,hello,bag,world`).

2. **Processing**:
   - The input string is split using `split(',')` to create a list of words.
   - The list is then sorted using `sort()`, which arranges the words in alphabetical order.

3. **Output**:
   - The sorted list is converted back into a string using `','.join()`, and it is printed as the final result.

---

## 🎯 Use Case

This program can be useful for sorting lists of words or creating alphabetically ordered lists for tasks such as indexing, categorizing, or organizing data.

---
