
# 📐 Program 30: Calculate the Natural Logarithm (Python)

This Python program calculates the **natural logarithm (ln)** of any positive number using the built-in `math` module.

---

## 📌 Problem Statement

**Write a Python program to calculate the natural logarithm of any number.**

---

## 🔍 What is the Natural Logarithm?

The **natural logarithm**, denoted as **ln(x)**, is the logarithm to the base **e**, where **e ≈ 2.71828**. 

### 🔁 Mathematical Definition:
If:
\[
\ln(x) = y \Rightarrow e^y = x
\]
Then:
- `x` must be a **positive number**
- `ln(x)` gives you the power to which **e** must be raised to get **x**

---

## 🧮 Formula

\[
\ln(x) = \log_e(x)
\]

Where:
- `x > 0`
- `e` is Euler’s number (`≈ 2.71828`)

---

## ✅ Sample Code

```python
import math

# Get user input
number = float(input("Enter a positive number to calculate its natural logarithm (ln): "))

# Check if input is valid
if number <= 0:
    print("Please enter a number greater than 0.")
else:
    # Calculate natural log
    result = math.log(number)
    print(f"The natural logarithm of {number} is: {result:.5f}")
```

---

## ▶️ Example Output

```bash
Enter a positive number to calculate its natural logarithm (ln): 5
The natural logarithm of 5.0 is: 1.60944
```

---

## 🔬 Where is ln(x) Used?

The natural logarithm is widely used in:

- 📊 **Mathematics**: Calculus, limits, integrals
- 🧪 **Physics**: Exponential decay, radioactive half-life
- 📈 **Economics**: Continuous compound interest
- 📡 **Engineering**: Signal processing, entropy

---

## ⚠️ Important Notes

- ln(x) is **undefined for x ≤ 0**
- The function `math.log(x)` in Python **defaults to base e**
- If you need log base 10, use `math.log10(x)`

---

## 📁 Suggested Project Structure

```
natural_logarithm/
├── natural_log.py
└── README.md
```

---

## 💡 Try This

- Add error handling for non-numeric input.
- Plot ln(x) values using `matplotlib`.
- Add a GUI using Tkinter for calculator-style input.

---

