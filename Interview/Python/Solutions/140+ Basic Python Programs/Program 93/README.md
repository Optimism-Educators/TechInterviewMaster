# Program93
Here’s **Program 93** written in the format you requested:

---

```markdown
# 🟩 Program 93: Radians to Degrees Conversion

This Python program defines a function `radians_to_degrees()` that takes an angle in radians and returns the corresponding angle in degrees, rounded to one decimal place.

---

## 📌 Problem Statement

Write a function `radians_to_degrees()` that converts an angle from radians to degrees and returns the result rounded to one decimal place.

The formula to convert radians to degrees is:
\[
\text{degrees} = \text{radians} \times \frac{180}{\pi}
\]

---

## 🧠 Concepts Used

- Mathematical Calculations
- Function Definition
- Radians to Degrees Conversion
- Rounding Function

---

## 🧪 Sample Code

```python
import math

def radians_to_degrees(radians):
    # Convert radians to degrees and round the result to one decimal place
    return round(radians * (180 / math.pi), 1)

# Test cases
print(radians_to_degrees(1))  # Output: 57.3
print(radians_to_degrees(20))  # Output: 1145.9
print(radians_to_degrees(50))  # Output: 2864.8
```

---

## 🎯 Example Input & Output

### Input

```
1
20
50
```

### Output

```
57.3
1145.9
2864.8
```

---

## ✅ Notes

- The function uses the `math.pi` constant for the value of π.
- The result is rounded to one decimal place using Python's built-in `round()` function.
- Make sure the input is in radians, as this conversion applies to radians only.

---

Let me know if you'd like any further adjustments! ✨

```
