
# ➕ Program 37: Add Two Matrices in Python

This Python program demonstrates how to **add two matrices** of the same dimension.

---

## 📌 Problem Statement

**Write a Python program to add two matrices.**

---

## 🧮 What is Matrix Addition?

Matrix addition is a mathematical operation where **corresponding elements** of two matrices are added together to form a new matrix.

✅ **Conditions**:
- Both matrices must have the **same number of rows and columns**.

### 📊 Example:

Matrix A:
```

1 2 3
4 5 6

```

Matrix B:
```

7 8 9
1 2 3

```

Resultant Matrix (A + B):
```

8 10 12
5 7 9

```

---

## ✅ Sample Code

```python
# Function to add two matrices
def add_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Sample Matrices
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8, 9], [1, 2, 3]]

# Adding the matrices
sum_matrix = add_matrices(A, B)

# Display the result
print("Sum of the matrices:")
for row in sum_matrix:
    print(row)
```

---

## ▶️ Example Output

```bash
Sum of the matrices:
[8, 10, 12]
[5, 7, 9]
```

---

## 📁 Suggested Project Structure

```
matrix_addition/
├── add_matrices.py
└── README.md
```

---

## 💡 Try It Yourself

- Input matrices from the user.
- Handle **dimension mismatch** errors gracefully.
- Extend the program to **multiply** matrices.

---
