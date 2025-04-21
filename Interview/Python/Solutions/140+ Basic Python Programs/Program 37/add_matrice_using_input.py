# Author: [Antim Pal](www.github.com/antimpal)
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

#Test the function
A=int(input("Enter the number of rows in matrix A: "))
B=int(input("Enter the number of columns in matrix A: "))
C=int(input("Enter the number of rows in matrix B: "))
D=int(input("Enter the number of columns in matrix B: "))
A = [[int(input("Enter element A{}{}: ".format(i+1, j+1))) for j in range(B)] for i in range(A)]
B = [[int(input("Enter element B{}{}: ".format(i+1, j+1))) for j in range(D)] for i in range(C)]    
print("Matrix A:", A)
print("Matrix B:", B)
# Call the function and print the result
result = add_matrices(A, B)
print("Resultant Matrix:", result)