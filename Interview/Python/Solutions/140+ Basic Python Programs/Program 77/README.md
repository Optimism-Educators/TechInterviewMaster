# Program77
Here is **Program 77** in the requested format:

---

```markdown
# 📝 Program 77: Remove Duplicates and Sort Words Alphanumerically

This Python program accepts a sequence of whitespace-separated words as input and then prints the words after removing all duplicates and sorting them alphanumerically.

---

## 📌 Problem Statement

**Write a Python program that accepts a sequence of whitespace-separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.**

### Example

Suppose the following input is supplied to the program:
- Input: `hello world and practice makes perfect and hello world again`

Then, the output of the program should be:
```

again and hello makes perfect practice world

```

---

## 💡 Explanation

1. **Input**:
   - The user is asked to input a sequence of words separated by whitespace.
   
2. **Logic**:
   - The input string is split into a list of words.
   - The set data structure is used to remove duplicate words, as sets do not allow duplicates.
   - The list is then sorted alphanumerically.
   - Finally, the sorted words are joined back into a single string, with each word separated by a space.
   
3. **Output**:
   - A string of words is printed, where duplicates are removed and the words are sorted alphanumerically.

---

## ✅ Sample Code

```python
# Function to remove duplicates and sort words alphanumerically
def remove_duplicates_and_sort(words):
    word_list = words.split()  # Split the input string into a list of words
    unique_words = set(word_list)  # Remove duplicates by converting the list to a set
    sorted_words = sorted(unique_words)  # Sort the unique words alphanumerically
    return ' '.join(sorted_words)  # Join the sorted words into a single string

# Input the whitespace-separated sequence of words
words = input("Enter words separated by whitespace: ")

# Get the sorted and deduplicated result
sorted_result = remove_duplicates_and_sort(words)

# Print the result
print(sorted_result)
```

---

## ▶️ Example Output

```bash
Enter words separated by whitespace: hello world and practice makes perfect and hello world again
again and hello makes perfect practice world
```

---

## 🔍 Explanation

1. **Input**:
   - The user is prompted to input a sequence of words separated by whitespace (e.g., `hello world and practice makes perfect and hello world again`).

2. **Processing**:
   - The input string is split using `split()` to create a list of words.
   - By converting the list to a set, duplicate words are automatically removed.
   - The remaining unique words are then sorted using `sorted()`.

3. **Output**:
   - The sorted list of unique words is converted back into a string using `' '.join()`, and it is printed as the final result.

---

## 🎯 Use Case

This program can be useful for cleaning up and organizing a list of words, such as for text processing, data analysis, or generating unique and sorted keyword lists.

---

Let me know if you'd like further clarifications or modifications! 😊

```

---

Let me know if you need any more adjustments or additional programs!
