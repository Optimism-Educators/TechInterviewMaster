
## 📘 Program 122 – List Operation with Divisibility

### 📝 Description  

This program defines a function `list_operation(x, y, n)` that generates an ordered list of numbers in a given range `[x, y]` (inclusive) which are divisible by the divisor `n`. If no numbers in the range are divisible by `n`, it returns an empty list.

### 🔍 Purpose  

The function takes three parameters:

1. `x`: The starting number of the range (inclusive).
2. `y`: The ending number of the range (inclusive).
3. `n`: The divisor used to filter numbers in the range.

It then returns a list of numbers in the range `[x, y]` that are divisible by `n`.

---

### ✅ Examples

```python
list_operation(1, 10, 3) ➞ [3, 6, 9]

list_operation(7, 9, 2) ➞ [8]

list_operation(15, 20, 7) ➞ []
```

---

### 💡 Function Logic

1. **Input**: The user provides a range `[x, y]` and a divisor `n`.
2. **Filtering**: The function iterates through the range `[x, y]` and checks if each number is divisible by `n` (i.e., `num % n == 0`).
3. **Return**: The function returns a list of numbers that are divisible by `n`. If none are divisible, it returns an empty list.

---

### 🧠 Function Definition

```python
def list_operation(x, y, n):
    return [num for num in range(x, y + 1) if num % n == 0]
```

---

### 🔁 How to Use

1. Call the `list_operation()` function with three arguments: `x`, `y`, and `n`.
   - `x` is the starting number (inclusive) of the range.
   - `y` is the ending number (inclusive) of the range.
   - `n` is the divisor used to filter numbers.
2. The function will return an ordered list of numbers in the range `[x, y]` that are divisible by `n`.

### 💡 Example Usage

```python
result = list_operation(1, 10, 3)
print(result)  # Output: [3, 6, 9]
```

---

### 🛠️ How It Works

- **Range**: The function generates numbers within the range `[x, y]` using the `range(x, y + 1)` function.
- **Divisibility**: For each number in the range, the function checks if it is divisible by `n` using the modulus operator (`%`).
- **Return**: The function returns a list of all numbers that are divisible by `n`. If no such numbers exist, an empty list is returned.

