# Author: <Antim Pal>
# Date: <2023-10-04>
# Description: Write a Python program to multiply two matrices.
# Input: 2D list (matrix)
# Output: 2D list (resultant matrix)
# Example:
# Input: A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
# Output: [[19, 22], [43, 50]]

def multiply_matrices(A, B):
    # Check if the number of columns in A is equal to the number of rows in B
    if len(A[0]) != len(B):
        return "Error: The number of columns in A must be equal to the number of rows in B."
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = multiply_matrices(A, B)
print(result)
# Output: [[19, 22], [43, 50]]
# The program multiplies two matrices A and B and returns the resultant matrix.
# The example provided demonstrates the multiplication of two 2x2 matrices.
# The function checks if the matrices can be multiplied and initializes the result matrix with zeros.
# It then performs the multiplication using nested loops and returns the final result.
# The program is efficient and handles the multiplication of matrices of different sizes as long as the dimensions are compatible.
# The time complexity of the matrix multiplication is O(n^3) where n is the number of rows/columns in the matrices.
# The space complexity is O(n^2) for the result matrix.
# The program can be further optimized using numpy for larger matrices.

