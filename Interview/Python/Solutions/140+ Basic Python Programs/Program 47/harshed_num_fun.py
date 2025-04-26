def is_harshad(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

number = int(input("Enter a number: "))

if is_harshad(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")
# ✅ Explanation:
# str(num) converts the number to a string to easily iterate over digits.

# The function is reusable and modular.