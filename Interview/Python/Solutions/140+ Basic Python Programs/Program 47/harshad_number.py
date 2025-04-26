number = int(input("Enter a number: "))
temp = number
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if number % digit_sum == 0:
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")
