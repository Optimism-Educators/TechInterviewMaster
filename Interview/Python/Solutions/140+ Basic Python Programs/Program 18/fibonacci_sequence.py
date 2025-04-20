# problem fabunacci sequence
# Problem Statement:
# Write a program to print the first N terms of the Fibonacci sequence.
# Input Format:
# Input consists of a single integer N.
# Output Format:
# The output consists of a single integer N representing the number of terms in the Fibonacci sequence.
# Sample Input:
# 5
# Sample Output:
# 0 1 1 2 3 5

# Author: Antim Pal
# Date: 202-04-20

# Time Complexity: O(N)
# Space Complexity: O(1)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")
print()

