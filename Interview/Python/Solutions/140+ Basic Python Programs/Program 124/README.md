# Program124
Here is the **README.md** file for **Program 124 – Secret Society Name**:

---

## 📘 Program 124 – Secret Society Name

### 📝 Description  

This program defines a function `society_name(names)` that generates a secret society name. The name is formed by taking the first letter of each friend's name, sorting them alphabetically, and then concatenating them together.

### 🔍 Purpose  

The function allows you to create a unique "secret society" name by sorting the first letters of a list of names alphabetically and combining them into a string.

---

### ✅ Examples

```python
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"
```

---

### 💡 Function Logic

1. **Input**: The function takes a list of names, where each name is a string.
2. **Process**:
   - The first letter of each name is extracted.
   - The letters are sorted alphabetically.
   - The sorted letters are concatenated to form the secret society name.
3. **Return**: The function returns the secret society name as a string.

---

### 🧠 Function Definition

```python
def society_name(names):
    return ''.join(sorted([name[0] for name in names]))
```

---

### 🔁 How to Use

1. Call the `society_name()` function with a list of names as the argument.
2. The function will return a string representing the secret society name, which is the first letter of each name sorted alphabetically.

### 💡 Example Usage

```python
result = society_name(["Adam", "Sarah", "Malcolm"])
print(result)  # Output: "AMS"
```

---

### 🛠️ How It Works

- **List Comprehension**: The function uses a list comprehension `[name[0] for name in names]` to extract the first letter of each name.
- **Sorting**: The `sorted()` function is used to sort the first letters alphabetically.
- **String Joining**: The `''.join()` method concatenates the sorted letters into a single string.

---

### 🧠 Example Walkthrough

For the input `["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]`, the function follows these steps:

- Extract first letters: `['P', 'C', 'R', 'R', 'M', 'J']`
- Sort them alphabetically: `['C', 'J', 'M', 'P', 'R', 'R']`
- Concatenate the letters: `"CJMPRR"`

---

Let me know if you need further changes or additions!
