class HarshadChecker:
    def __init__(self, number):
        self.number = number

    def is_harshad(self):
        digit_sum = sum(int(d) for d in str(self.number))
        return self.number % digit_sum == 0

# Input from user
num = int(input("Enter a number: "))
checker = HarshadChecker(num)

if checker.is_harshad():
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")


# ✅ Explanation:
# We use a class to encapsulate the logic.

# This is scalable for more number-related checks in the future.