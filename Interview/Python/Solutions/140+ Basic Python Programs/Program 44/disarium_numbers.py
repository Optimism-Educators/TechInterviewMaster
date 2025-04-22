# Author: <Antim Pal>
# Date: <27/08/2020>
# Discription: Write a Python program to check if a number is a Disarium Number.
# i want to print 1 to 100 print all disarium numbers from 1 to 100
# Disarium number is a number where the sum of its digits powered with their respective positions is equal to the number itself.
# Example: 135 is a Disarium number because 1^1 + 3^2 + 5^3 = 135.

def disarium_number(n):
    sum = 0
    for i in range(1, len(str(n)) + 1):
        sum += int(str(n)[i - 1]) ** i
    return sum == n

# Print all Disarium numbers from 1 to 100
for j in range(1, 101):
    if disarium_number(j):
        print(j)
        
print(" This is the main sub program")
