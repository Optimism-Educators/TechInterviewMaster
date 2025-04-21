# Author: <Antim Pal>
# Date: <16-08-2021>

# Python program to transpose a matrix
# using zip function

def printTranspose(mat):
    for row in zip(*mat):
        print(row)


# Driver code
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

printTranspose(mat)
# Eplamations:
# In this program, we have used the zip() function to transpose a matrix. The zip() function takes iterable elements as
# input, and returns an iterator of tuples. Each tuple contains one element from each of the input iterables. If the input
# iterables do not contain enough elements, missing values are filled by None in the output tuple, until all the input
# iterables are exhausted.