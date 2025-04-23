# Author: <Antim Pal>
# Date: <21-04-2025>
# Description: Write a Python program to find the sum of cubes of first n natural numbers.
# Input: 3
# Output: 36
# Explanation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
# Approach:
# 1. Define a function `sum_of_cubes` that takes an integer `n` as input.
# 2. Initialize a variable `sum_cubes` to 0.
# 3. Use a for loop to iterate from 1 to `n` (inclusive).
# 4. In each iteration, add the cube of the current number to `sum_cubes`.
# 5. After the loop, return `sum_cubes`.
# 6. In the main block, take user input for `n`, call the function, and print the result.
# 7. The program will output the sum of cubes of the first `n` natural numbers.
# 8. The time complexity of this program is O(n) and the space complexity is O(1).
def sum_of_cubes(n):
    sum_cubes = 0
    for i in range(1, n + 1):
        sum_cubes += i ** 3
    return sum_cubes
n = int(input("Enter a number: "))
result = sum_of_cubes(n)
print("The sum of cubes of the first", n, "natural numbers is:", result)

# Test cases
# Test case 1: n = 3
# Expected output: 36
# Test case 2: n = 4
# Expected output: 100
# Test case 3: n = 5
# Expected output: 225