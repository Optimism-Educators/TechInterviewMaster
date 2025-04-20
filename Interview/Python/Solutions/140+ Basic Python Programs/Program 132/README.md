# Program132
Here is the **README.md** file for **Program 132 – Amplify Numbers**:

---

## 📘 Program 132 – Amplify Numbers

### 📝 Description  

This program defines a function `amplify()` that takes an integer `n` and returns a list of numbers from `1` to `n`. If a number in the list is divisible by 4, it is amplified (multiplied by 10). If it is not divisible by 4, it remains unchanged. The function should return the final list based on these conditions.

### 🔍 Purpose  

The function allows us to modify numbers in a list based on divisibility by 4, amplifying those that are divisible by 4, which can be useful for specific calculations or transformations in mathematical tasks.

---

### ✅ Examples

```python
amplify(4) ➞ [1, 2, 3, 40]

amplify(3) ➞ [1, 2, 3]

amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
```

---

### 💡 Function Logic

1. **Input**: The function takes an integer `n`.
2. **Process**:
   - Iterate through the numbers from `1` to `n`.
   - For each number:
     - If it is divisible by 4, multiply it by 10.
     - If it is not divisible by 4, keep the number unchanged.
3. **Return**: The function returns the modified list of numbers.

---

### 🧠 Function Definition

```python
def amplify(n):
    return [x * 10 if x % 4 == 0 else x for x in range(1, n + 1)]
```

---

### 🔁 How to Use

1. Call the `amplify()` function with an integer `n` as input.
2. The function will return a list of numbers from `1` to `n`, with multiples of 4 amplified by 10.

### 💡 Example Usage

```python
result = amplify(4)
print(result)  # Output: [1, 2, 3, 40]
```

---

### 🧠 Example Walkthrough

For the input `4`:

- Numbers: `[1, 2, 3, 4]`.
- `1`, `2`, and `3` are not divisible by 4, so they remain unchanged.
- `4` is divisible by 4, so it is multiplied by 10 to give `40`.
- The final list is `[1, 2, 3, 40]`.

For the input `25`:

- Numbers: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]`.
- Numbers like `4`, `8`, `12`, `16`, `20`, and `24` are divisible by 4 and are amplified by 10.
- The final list is `[1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]`.

---

### 🧠 Additional Notes

- The function handles numbers greater than or equal to `1`.
- **Edge Cases**:
  - If `n` is 1, the list will only contain `[1]`, and no amplification will occur.
  - The function can work for any positive integer `n`, returning the list from `1` to `n`.

---

### 🔍 Example Input/Output

- **Input**: `4`
  - **Output**: `[1, 2, 3, 40]`
  
- **Input**: `3`
  - **Output**: `[1, 2, 3]`
  
- **Input**: `25`
  - **Output**: `[1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]`

---

Let me know if you need any further modifications!
