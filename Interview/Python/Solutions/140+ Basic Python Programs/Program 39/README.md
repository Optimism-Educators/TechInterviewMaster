
# 🔄 Program 39: Transpose a Matrix in Python

This Python program transposes a given matrix. Transposing a matrix involves flipping it over its diagonal, turning rows into columns and vice versa.

---

## 📌 Problem Statement

**Write a Python program to find the transpose of a matrix.**

---

## 🔢 What is Transpose of a Matrix?

The **transpose of a matrix** is a new matrix whose rows are the columns of the original.  
If the original matrix is **A (m×n)**, then its transpose is **Aᵀ (n×m)**.

### 🧮 Example

Original Matrix:

\[
A = \begin{bmatrix}1 & 2 & 3\\4 & 5 & 6\end{bmatrix}
\]

Transposed Matrix:

\[
Aᵀ = \begin{bmatrix}1 & 4\\2 & 5\\3 & 6\end{bmatrix}
\]

---

## ✅ Sample Code

```python
# Function to transpose a matrix
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose the matrix
transposed = transpose_matrix(matrix)

# Display result
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
```

---

## ▶️ Example Output

```bash
Original Matrix:
[1, 2, 3]
[4, 5, 6]

Transposed Matrix:
[1, 4]
[2, 5]
[3, 6]
```

---

## 📁 Suggested Project Structure

```
matrix_transpose/
├── transpose_matrix.py
└── README.md
```

---

## 💡 Try It Yourself

- Transpose a square or non-square matrix from **user input**.
- Use `zip()` for a more Pythonic approach:

  ```python
  transposed = list(map(list, zip(*matrix)))
  ```

- Use NumPy for faster processing:

  ```python
  import numpy as np
  result = np.transpose(matrix)
  ```

