
## 📘 Program 128 – Multiply Numbers from String

### 📝 Description  

This program defines a function `multiply_nums()` that takes a string of numbers separated by a comma and a space, then returns the product of those numbers. The function handles multiple numbers in a string and computes the result accordingly.

### 🔍 Purpose  

The function extracts the numbers from the given string and computes their product. It handles edge cases such as zero in the string, negative numbers, and varying numbers of elements.

---

### ✅ Examples

```python
multiply_nums("2, 3") ➞ 6         # 2 * 3 = 6

multiply_nums("1, 2, 3, 4") ➞ 24  # 1 * 2 * 3 * 4 = 24

multiply_nums("54, 75, 453, 0") ➞ 0  # 54 * 75 * 453 * 0 = 0

multiply_nums("10, -2") ➞ -20     # 10 * -2 = -20
```

---

### 💡 Function Logic

1. **Input**: The function takes a string of numbers separated by commas and spaces.
2. **Process**:
   - Split the string by commas and spaces to extract the individual numbers.
   - Convert each string number to an integer.
   - Multiply all the integers together to compute the product.
3. **Return**: The function returns the computed product.

---

### 🧠 Function Definition

```python
def multiply_nums(nums):
    # Split the string by ', ' and map each part to an integer
    numbers = map(int, nums.split(", "))
    
    # Return the product of the numbers using the reduce function
    from functools import reduce
    return reduce(lambda x, y: x * y, numbers)
```

---

### 🔁 How to Use

1. Call the `multiply_nums()` function with a string of numbers separated by a comma and space.
2. The function will return the product of those numbers.

### 💡 Example Usage

```python
result = multiply_nums("2, 3")
print(result)  # Output: 6
```

---

### 🧠 Example Walkthrough

For the input `"2, 3"`, the function follows these steps:

- Split the string: `['2', '3']`.
- Convert the strings to integers: `[2, 3]`.
- Compute the product: `2 * 3 = 6`.

For the input `"1, 2, 3, 4"`, the function:

- Splits the string: `['1', '2', '3', '4']`.
- Converts to integers: `[1, 2, 3, 4]`.
- Computes the product: `1 * 2 * 3 * 4 = 24`.

---

### 🛠️ How It Works

- **String Splitting**: The string is split using `.split(", ")`, separating the numbers by the comma and space.
- **Conversion to Integers**: The `map(int, ...)` function converts each number (as a string) to an integer.
- **Product Calculation**: The `reduce()` function from the `functools` module is used to calculate the product of all numbers in the list.

---

### 🔍 Example Input/Output

- **Input**: `"2, 3"`
  - **Output**: `6`
  
- **Input**: `"1, 2, 3, 4"`
  - **Output**: `24`
  
- **Input**: `"54, 75, 453, 0"`
  - **Output**: `0`
