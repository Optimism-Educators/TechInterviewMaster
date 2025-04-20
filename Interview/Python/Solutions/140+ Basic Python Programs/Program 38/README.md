
# ✖️ Program 38: Multiply Two Matrices in Python

This Python program multiplies two matrices using **nested loops**, given that the number of columns in the first matrix equals the number of rows in the second.

---

## 📌 Problem Statement

**Write a Python program to multiply two matrices.**

---

## 🔢 What is Matrix Multiplication?

Matrix multiplication is a binary operation that produces a new matrix from two matrices.  
For two matrices **A (m×n)** and **B (n×p)**, the result will be a new matrix **C (m×p)**.

### ✅ Condition for Matrix Multiplication:
- The number of **columns in Matrix A** must be equal to the number of **rows in Matrix B**.

---

## 🧮 Formula

\[
C[i][j] = \sum_{k=0}^{n} A[i][k] \times B[k][j]
\]

---

## ✅ Sample Code

```python
# Function to multiply two matrices
def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example Matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 4], [2, 5], [3, 6]]

# Multiply matrices
product = multiply_matrices(A, B)

# Display the result
print("Product of the matrices:")
for row in product:
    print(row)
```

---

## ▶️ Example Output

```bash
Product of the matrices:
[14, 32]
[32, 77]
```

---

## 📁 Suggested Project Structure

```
matrix_multiplication/
├── multiply_matrices.py
└── README.md
```

---

## 💡 You Can Try

- Get matrix inputs from the user.
- Use NumPy for faster computation:

  ```python
  import numpy as np
  result = np.dot(A, B)
  ```

- Validate dimensions and show user-friendly error messages.

---
