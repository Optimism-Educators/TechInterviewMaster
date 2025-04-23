# Author: <Antim Pal>
# Date: 21-04-2025
# Description: Write a Python program to find the largest element in an array.
# Input: [1, 2, 3, 4, 5]
# Output: 5
# Input: [5, 4, 3, 2, 1]
# Output: 5

# Solution 1: Using max() function
# This function takes an array as input and returns the largest element in the array.
# The max() function is a built-in function in Python that returns the largest of the input values.
# It can take any number of arguments and returns the largest one.
# In this case, we are passing the entire array as a single argument to the max() function.
def largest_element(arr):
    return max(arr)

# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(largest_element(arr))
    
