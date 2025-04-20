
# 📝 Program 75: Generate a 2-Dimensional Array Based on Input Digits

This Python program takes two input digits, `X` and `Y`, and generates a 2-dimensional array where each element in the array is the product of its row index (`i`) and column index (`j`).

---

## 📌 Problem Statement

**Write a Python program that takes 2 digits, X and Y, as input and generates a 2-dimensional array.**

- The element value in the i-th row and j-th column of the array should be `i * j`.
- **Constraints**: 
  - i = 0, 1, ..., X-1
  - j = 0, 1, ..., Y-1

### Example

Suppose the following inputs are given to the program:
- Input: `3, 5`

Then, the output of the program should be:
```

[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8]]

```

---

## 💡 Explanation

1. **Input**:
   - Two integers `X` and `Y` are taken as input.
   
2. **Logic**:
   - The program generates a 2D list where the element in the i-th row and j-th column is `i * j`.
   - The program iterates over the rows and columns, filling the array with the respective products.

3. **Output**:
   - A 2-dimensional list (array) is generated and printed.

---

## ✅ Sample Code

```python
# Function to generate 2D array
def generate_2d_array(X, Y):
    array = [[i * j for j in range(Y)] for i in range(X)]
    return array

# Input X and Y
X, Y = map(int, input("Enter two numbers (X Y): ").split(','))

# Generate the 2D array
result = generate_2d_array(X, Y)

# Print the result
print(result)
```

---

## ▶️ Example Output

```bash
Enter two numbers (X Y): 3,5
[[0, 0, 0, 0, 0], 
 [0, 1, 2, 3, 4], 
 [0, 2, 4, 6, 8]]
```

---

## 🔍 Explanation

1. **Input**:
   - The user is prompted to input two values, `X` and `Y`, which represent the number of rows and columns, respectively.

2. **2D Array Generation**:
   - The list comprehension `[[i * j for j in range(Y)] for i in range(X)]` creates the 2D array.
   - For each `i` in the range `0` to `X-1` (rows), and for each `j` in the range `0` to `Y-1` (columns), the program calculates the product `i * j`.

3. **Output**:
   - The program prints the generated 2D array.

---

## 🎯 Use Case

This type of program is useful for generating tables, matrices, or grids where the value of each element is defined based on its position (like multiplication tables).

---

Let me know if you'd like further clarifications or adjustments to the program! 😊

```

---

Feel free to ask for any changes or additional information!
