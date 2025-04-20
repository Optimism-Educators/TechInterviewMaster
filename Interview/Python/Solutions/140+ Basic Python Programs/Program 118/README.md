# Program118
Here's the **README.md** file for **Program 118 – Sum of Budgets**:

---

## 📘 Program 118 – Sum of Budgets

### 📝 Description  

This program defines a function `get_budgets(lst)` that takes a list of dictionaries, where each dictionary contains information about a person (such as their name, age, and budget). The function calculates and returns the sum of the budgets of all the people in the list.

---

### ✅ Examples

```python
get_budgets([
  { 'name': 'John', 'age': 21, 'budget': 23000 },
  { 'name': 'Steve', 'age': 32, 'budget': 40000 },
  { 'name': 'Martin', 'age': 16, 'budget': 2700 }
]) ➞ 65700

get_budgets([
  { 'name': 'John', 'age': 21, 'budget': 29000 },
  { 'name': 'Steve', 'age': 32, 'budget': 32000 },
  { 'name': 'Martin', 'age': 16, 'budget': 1600 }
]) ➞ 62600
```

---

### 💡 Function Logic

- Iterate over the list of dictionaries.
- Access the value of the `budget` key in each dictionary.
- Sum up all the budgets.
- Return the total sum of the budgets.

---

### 🧠 Function Definition

```python
def get_budgets(lst):
    return sum(person['budget'] for person in lst)
```

---

### 🔁 How to Use

1. Provide a list of dictionaries, where each dictionary contains keys: `name`, `age`, and `budget`.
2. Call the `get_budgets()` function with the list as the argument.
3. The function returns the sum of all the budgets.

