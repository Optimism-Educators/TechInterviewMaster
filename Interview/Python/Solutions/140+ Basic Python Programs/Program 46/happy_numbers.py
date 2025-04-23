# Author: <Antim Pal>
# Date: 28/05/2020
# Discription:


def is_happy_number(num):
     seen = set()
     while num != 1 and num not in seen:
          seen.add(num)
          num = sum(int(digit) ** 2 for digit in str(num))
     return num == 1
number = int(input("Enter a number to check if it's a happy number: "))
if is_happy_number(number):
     print(f"{number} is a Happy Number!")
else:
     print(f"{number} is not a Happy Number.")
     
     
print("Happy Numbers between 1 and 100:")
for i in range(1, 101):
     if is_happy_number(i):
          print(i, end=" ")