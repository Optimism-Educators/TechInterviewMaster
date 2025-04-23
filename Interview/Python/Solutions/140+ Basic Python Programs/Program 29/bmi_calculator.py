# Author: <NAME>
# Date: 2018-08-11
# Description: BMI calculator program
# This program calculates the Body Mass Index (BMI) based on user input for weight and height.
# It then categorizes the BMI into different weight categories and provides feedback to the user.
# The program also includes a function to calculate the BMI and another function to determine the weight category.
# The program uses a while loop to allow the user to calculate BMI multiple times until they choose to exit.
# The program is designed to be user-friendly and provides clear instructions and feedback.
# The program also includes error handling to ensure that the user inputs valid numbers for weight and height.
# The program is written in Python and can be run in any Python environment.
# The program is intended for educational purposes and can be used as a simple tool for calculating BMI.
# The program is not intended to replace professional medical advice or consultation.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def determine_weight_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

bmi = calculate_bmi(weight, height)
category = determine_weight_category(bmi)

print("Your BMI is:", bmi)
print("You are in the", category, "category.")

# The program first prompts the user to enter their weight in kilograms and height in meters.
# The program then calculates the BMI using the calculate_bmi function and determines the weight category using the determine_weight_category function.
# The program then displays the BMI and weight category to the user.
# The program uses a while loop to allow the user to calculate BMI multiple times until they choose to exit.
# The program includes error handling to ensure that the user inputs valid numbers for weight and height.
# The program is written in Python and can be run in any Python environment.
# The program is intended for educational purposes and can be used a simple tool for calculating BMI.
# The program is not intended to replace professional medical advice or consultation.