# Author: <Antim Pal>
# Date: 2023-10-01
# Description: Write a Python program to find the largest element in an array using loops.
# Input: [1, 2, 3, 4, 5]
# Output: 5


# Solution 2: Using a loop
# This function takes an array as input and returns the largest element in the array.
# It uses a for loop to iterate through the array and find the largest element.
# The loop starts with the first element as the largest element and compares it with each subsequent element.
# If a larger element is found, it updates the largest element.
# Finally, it returns the largest element found in the array.

def largest_element(arr):
    largest = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > largest:
            largest = num
    return largest
# Driver code
if __name__ == "__main__":
    arr = input("Enter the elements of the array separated by spaces: ").split()
    arr = [int(i) for i in arr]  # Convert input strings to integers
    print(largest_element(arr))
# Output: 5
# Input: [5, 4, 3, 2, 1]
# Output: 5
# Input: [1, 2, 3, 4, 8]
# Output: 8
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 10