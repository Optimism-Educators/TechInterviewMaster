# Author: <Antim Pal>
# Date: 21-04-2025

# Description: Write a Python program to add two matrices using nested loops.
# Input: 2D list of integers
# Output: 2D list of integers
# Example:
# Input: A = [[1, 2, 3], [4, 5, 6]], B = [[7, 8, 9], [10, 11, 12]]
# Output: [[8, 10, 12], [14, 16, 18]]
def add_matrices(A, B):
    # Check if the dimensions of the matrices are the same
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]

    # Add the matrices using nested loops
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

    return result



# Example usage
if __name__ == "__main__":
    # Example matrices
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8, 9], [10, 11, 12]]

    # Add the matrices
    result = add_matrices(A, B)

    # Print the result
    print("Matrix A:", A)
    print("Matrix B:", B)
    print("Resultant Matrix:", result)

"""
Output:
Matrix A: [[1, 2, 3], [4, 5, 6]]
Matrix B: [[7, 8, 9], [10, 11, 12]]
Resultant Matrix: [[8, 10, 12], [14, 16, 18]]
"""
# Time Complexity: O(n*m), where n is the number of rows and m is the number of columns in the matrices.
# Space Complexity: O(n*m), as we are creating a new matrix to store the result.
# Note: This program assumes that the input matrices are non-empty and rectangular (all rows have the same number of columns).
# The program can be modified to handle different dimensions or empty matrices if needed.
# The program can be tested with different matrices to ensure its correctness.
# The program can be further optimized by using numpy for matrix operations, which is more efficient for large matrices.
# The program can be extended to handle matrix subtraction, multiplication, and other operations as needed.