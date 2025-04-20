# Program29
Certainly! Here's a detailed and structured explanation for **Program 29 – Calculating Body Mass Index (BMI) in Python**:

---

```markdown
# 🏋️‍♂️ Program 29: Calculate Body Mass Index (BMI) (Python)

This Python program calculates an individual's **Body Mass Index (BMI)** based on their weight and height.

---

## 📌 Problem Statement

**Write a Python program to calculate your Body Mass Index (BMI).**

---

## 🔢 What is Body Mass Index (BMI)?

**BMI** is a measure of body fat based on an individual's weight and height. It is commonly used as a screening tool to categorize individuals into different weight status categories, such as:

- Underweight
- Normal weight
- Overweight
- Obesity

### BMI Formula:

For the **metric system** (kg and meters):
\[
\text{BMI} = \frac{\text{weight (kg)}}{\text{height (m)}^2}
\]

For the **imperial system** (pounds and inches):
\[
\text{BMI} = \frac{\text{weight (lbs)}}{\text{height (in)}^2} \times 703
\]

---

## ✅ Sample Code

```python
# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula (metric system)
    bmi = weight / (height ** 2)
    return bmi

# Function to determine the BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Get input from user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display the result
print(f"Your BMI is: {bmi:.2f}")
print(f"Your weight category is: {bmi_category(bmi)}")
```

---

## ▶️ Example Output

```bash
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
Your weight category is: Normal weight
```

---

## 📊 BMI Categories

- **Underweight**: BMI < 18.5
- **Normal weight**: 18.5 ≤ BMI < 24.9
- **Overweight**: 25 ≤ BMI < 29.9
- **Obesity**: BMI ≥ 30

---

## 🧠 Important Notes

- **Accuracy**: BMI is a general indicator and does not measure body fat directly. It may not be accurate for athletes with high muscle mass or individuals with different body compositions.
- **Units**: Make sure to input the correct units (kg and meters for the metric system; lbs and inches for the imperial system).
- **Health Risks**: BMI is a useful tool for identifying potential health risks associated with underweight, overweight, or obesity.

---

## 📁 Suggested Project Structure

```
bmi_calculator/
├── bmi_calculator.py
└── README.md
```

---

## 💡 Bonus Ideas

- Add support for **imperial units** (lbs and inches).
- Include **error handling** to ensure valid inputs (e.g., negative numbers or zero).
- Provide health tips based on BMI results (e.g., exercise or diet recommendations).

---

Happy Coding! 🧠💡💪

```

Let me know if you'd like further enhancements or additional features for the program!
