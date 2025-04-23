# Author: <Antim Pal>
# Date: <21-04-2025>
# Description: Write a Python program to rotate a list to the right by a given number of steps.
# Input: [1, 2, 3, 4, 5], 2   
# Output: [4, 5, 1, 2, 3]
def right_rotate(lst, steps):
     """
     Rotate a list to the right by a given number of steps.
     
     Parameters:
     lst (list): The list to be rotated.
     steps (int): The number of steps to rotate the list.
     
     Returns:
     list: The rotated list.
     """
     if not lst:
          return lst
     steps = steps % len(lst)  # Handle cases where steps > len(lst)
     return lst[-steps:] + lst[:-steps]
print(right_rotate([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5, 1, 2]
print(right_rotate([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(right_rotate([1, 2, 3, 4, 5], 0))  # Output: [1, 2, 3, 4, 5]

