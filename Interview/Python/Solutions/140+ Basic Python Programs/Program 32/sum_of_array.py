# Author: <Antim Pal>
# Date: <21-04-2025>
# Description: Write a Program to find the sum of all elements in an array.
# Input: [1, 2, 3, 4, 5]
# Output: 15
# Explanation: The sum of all elements in the array is 1 + 2 + 3 + 4 + 5 = 15.
# Approach: Use the built-in sum() function to calculate the sum of all elements in the array.
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of space for the sum variable.
# Example: sum_of_array([1, 2, 3, 4, 5]) should return 15
def sum_of_array(arr):
    """
    Function to find the sum of all elements in an array.
    
    Parameters:
    arr (list): List of numbers
    
    Returns:
    int: Sum of all elements in the array
    """
    return sum(arr)

# Fixed the issue where 'arr' was being treated as an integer instead of a list.
arr = []
num_elements = int(input("Enter the number of elements in the array: "))
for i in range(num_elements):
    arr.append(int(input("Enter the elements of the array: ")))

# Example usage
print(sum_of_array(arr))  # Output will depend on user input
