# Author: <Antim Pal>
# Date: 21-04-2025
# Description: Write a Python program to rotate a list to the left by a given number of steps.
# Input: [1, 2, 3, 4, 5], 2
# Output: [3, 4, 5, 1, 2]

def left_rotation(lst, steps):
    return lst[steps:] + lst[:steps]

lst = [1, 2, 3, 4, 5]
steps = 2
print(left_rotation(lst, steps))
# Output: [3, 4, 5, 1, 2]
