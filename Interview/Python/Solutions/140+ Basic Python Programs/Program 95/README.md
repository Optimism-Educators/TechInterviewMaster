
# 🟩 Program 95: Area of a Hexagon

This Python program calculates the area of a regular hexagon given the side length \( x \).

---

## 📌 Problem Statement

The area \( A \) of a regular hexagon can be calculated using the formula:

\[
A = \frac{3 \cdot \sqrt{3}}{2} \cdot x^2
\]

Where \( x \) is the side length of the hexagon.

### Example:

For `x = 1`:
- The area will be approximately `2.6`.

For `x = 2`:
- The area will be approximately `10.4`.

For `x = 3`:
- The area will be approximately `23.4`.

---

## 🧠 Concepts Used

- Mathematical Formula for Area
- Square of a Number
- Square Root Function

---

## 🧪 Sample Code

```python
import math

def area_of_hexagon(x):
    # Formula for area of a regular hexagon
    area = (3 * math.sqrt(3) / 2) * (x ** 2)
    return round(area, 1)

# Test cases
print(area_of_hexagon(1))  # Output: 2.6
print(area_of_hexagon(2))  # Output: 10.4
print(area_of_hexagon(3))  # Output: 23.4
```

---

## 🎯 Example Input & Output

### Input

```
1
2
3
```

### Output

```
2.6
10.4
23.4
```

---

## ✅ Notes

- The `math.sqrt()` function is used to calculate the square root of 3 in the area formula.
- The result is rounded to one decimal place using the `round()` function for better readability.

---