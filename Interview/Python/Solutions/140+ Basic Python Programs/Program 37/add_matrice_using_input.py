# Author: [Antim Pal](www.github.com/antimpal)
# Date: 21-04-2025
# Description: Write a Python program to add two matrices using nested loops.
# Input: 2D list of integers
# Output: 2D list of integers


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