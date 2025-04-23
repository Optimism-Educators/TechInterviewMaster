# Author: Antim Pal
# DateL: 22-04-2025
# Title: disarium number
# discription: A number is called disarium if sum of its digits powered with their respective positions is equal to the number itself. For example, 135 is a disarium number as 1^1 + 3^2 + 5^3 = 135.
# 

def is_disarium(num):
    num_str = str(num)
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i]) ** (i+1)
    return sum == num

num = int(input("Enter a number: "))
if is_disarium(num):
    print(num, "is a disarium number.")
else:
    print(num, "is not a disarium number.")
    
# Example: 
# Enter a number: 135
# 135 is a disarium number.
# Enter a number: 123
# 123 is not a disarium 

#Explantion: 