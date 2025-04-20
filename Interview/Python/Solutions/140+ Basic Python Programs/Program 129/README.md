
## 📘 Program 129 – Square Digits of a Number

### 📝 Description  

This program defines a function `square_digits()` that takes an integer and returns an integer with each of the digits squared. The function processes each digit in the number, squares it, and then returns the result as a new number formed by the squared digits.

### 🔍 Purpose  

The function iterates through each digit of the number, squares the digit, and concatenates the squared values together to form a new integer. The function should handle multi-digit numbers and return a valid integer.

---

### ✅ Examples

```python
square_digits(9119) ➞ 811181  # 9^2 = 81, 1^2 = 1, 1^2 = 1, 9^2 = 81 ➞ 811181

square_digits(2483) ➞ 416649  # 2^2 = 4, 4^2 = 16, 8^2 = 64, 3^2 = 9 ➞ 416649

square_digits(3212) ➞ 9414    # 3^2 = 9, 2^2 = 4, 1^2 = 1, 2^2 = 4 ➞ 9414
```

---

### 💡 Function Logic

1. **Input**: The function takes an integer as input.
2. **Process**:
   - Convert the integer to a string to easily access individual digits.
   - Square each digit and convert it back to a string.
   - Concatenate the squared digits to form the final result.
   - Convert the final concatenated string back into an integer.
3. **Return**: The function returns the new integer formed by the squared digits.

---

### 🧠 Function Definition

```python
def square_digits(num):
    # Convert the number to a string to access each digit
    return int(''.join(str(int(i) ** 2) for i in str(num)))
```

---

### 🔁 How to Use

1. Call the `square_digits()` function with an integer as input.
2. The function will return a new integer where each digit of the input integer is squared.

### 💡 Example Usage

```python
result = square_digits(9119)
print(result)  # Output: 811181
```

---

### 🧠 Example Walkthrough

For the input `9119`, the function follows these steps:

- Convert the number `9119` to the string `"9119"`.
- Square each digit: `9^2 = 81`, `1^2 = 1`, `1^2 = 1`, `9^2 = 81`.
- Concatenate the squared digits: `"81" + "1" + "1" + "81" = "811181"`.
- Convert the final result back to an integer: `811181`.

For the input `2483`, the function:

- Converts `2483` to the string `"2483"`.
- Squares each digit: `2^2 = 4`, `4^2 = 16`, `8^2 = 64`, `3^2 = 9`.
- Concatenates the squared digits: `"4" + "16" + "64" + "9" = "416649"`.
- Converts the final result back to an integer: `416649`.

---

### 🧠 Additional Notes

- **Edge Cases**:
  - The function works with any positive integer.
  - The function handles multiple digits and ensures that the final output is a valid integer.

---

### 🔍 Example Input/Output

- **Input**: `9119`
  - **Output**: `811181`
  
- **Input**: `2483`
  - **Output**: `416649`
  
- **Input**: `3212`
  - **Output**: `9414`
