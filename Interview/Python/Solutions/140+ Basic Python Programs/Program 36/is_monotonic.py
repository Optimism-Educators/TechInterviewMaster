# Author: <Antim Pal>
# Date: <2023-05-29>
# Description: Python program to check if a list is sorted  in non-increasing or non-decreasing order.
# Time Complexity: O(n)      
# Space Complexity: O(1)
# Approach:
# 1. Initialize two boolean variables, increasing and decreasing, to True.
# 2. Iterate through the list from the first element to the second last element.
# 3. Compare each element with the next element.
# 4. If the current element is greater than the next element, set increasing to False.
# 5. If the current element is less than the next element, set decreasing to False.
# 6. If both increasing and decreasing are False, break the loop.
# 7. After the loop, check if either increasing or decreasing is True.
# 8. If either is True, return True (the list is monotonic).
# 9. If both are False, return False (the list is not monotonic).
# 10. Test the function with different cases.
# 11. Print the results.


def is_monotonic(arr):
     increasing = True
     decreasing = True
     
     for i in range(len(arr) - 1):
          if arr[i] > arr[i + 1]:
               increasing = False
          if arr[i] < arr[i + 1]:
               decreasing = False
          if not increasing and not decreasing:
               break
     
     return increasing or decreasing    
     
# Test cases
print(is_monotonic([1, 2, 2, 3]))  # Output: True
print(is_monotonic([1, 3, 2]))  # Output: False
print(is_monotonic([3, 2, 1]))  # Output: True
print(is_monotonic([1, 1, 1]))  # Output: True
print(is_monotonic([1, 2, 3, 4, 5]))  # Output: True
print(is_monotonic([5, 4, 3, 2, 1]))  # Output: True
print(is_monotonic([1, 2, 3, 2, 1]))  # Output: False  x