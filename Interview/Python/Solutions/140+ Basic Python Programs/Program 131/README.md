# Program131
Here is the **README.md** file for **Program 131 – Mean of All Digits**:

---

## 📘 Program 131 – Mean of All Digits

### 📝 Description  

This program defines a function `mean()` that takes an integer as input and returns the mean (average) of all the digits of that number. The mean is calculated by summing the digits of the number and dividing the sum by the total number of digits.

### 🔍 Purpose  

The function helps calculate the average of digits in a given number. This can be useful in scenarios where you need to find the central tendency of a number's digits or perform statistical analysis on digits.

---

### ✅ Examples

```python
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6
```

---

### 💡 Function Logic

1. **Input**: The function takes an integer as input.
2. **Process**:
   - Convert the integer to a string to easily access individual digits.
   - Sum all the digits.
   - Divide the sum by the number of digits to find the mean.
3. **Return**: The function returns the mean of the digits as an integer.

---

### 🧠 Function Definition

```python
def mean(n):
    # Convert the number to string to access digits
    digits = [int(digit) for digit in str(n)]
    
    # Calculate the sum of digits
    total_sum = sum(digits)
    
    # Return the mean of the digits
    return total_sum // len(digits)
```

---

### 🔁 How to Use

1. Call the `mean()` function with an integer as input.
2. The function will return the mean of all digits in that integer.

### 💡 Example Usage

```python
result = mean(42)
print(result)  # Output: 3
```

---

### 🧠 Example Walkthrough

For the input `42`:

- Convert `42` to its individual digits: `[4, 2]`.
- Sum the digits: `4 + 2 = 6`.
- Divide the sum by the number of digits: `6 / 2 = 3`.
- The mean is `3`.

For the input `12345`:

- Convert `12345` to its individual digits: `[1, 2, 3, 4, 5]`.
- Sum the digits: `1 + 2 + 3 + 4 + 5 = 15`.
- Divide the sum by the number of digits: `15 / 5 = 3`.
- The mean is `3`.

---

### 🧠 Additional Notes

- The mean will always be an integer because the sum of the digits is always divisible by the number of digits.
- **Edge Cases**:
  - If the number has only one digit, the mean will be the number itself.
  - If the input number is 0, the mean is also 0.

---

### 🔍 Example Input/Output

- **Input**: `42`
  - **Output**: `3`
  
- **Input**: `12345`
  - **Output**: `3`
  
- **Input**: `666`
  - **Output**: `6`

---

Let me know if you need any further modifications!
