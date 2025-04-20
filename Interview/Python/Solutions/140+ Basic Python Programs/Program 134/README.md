# Program134
# 🟠 Circle Class

A lightweight Python class to calculate the **area** and **perimeter** of a circle given its radius.

---

## 📌 Description

The `Circle` class provides two methods:

- `getArea()` – Returns the area of the circle, rounded to the nearest whole number.
- `getPerimeter()` – Returns the perimeter (circumference), also rounded.

---

## 🔧 Usage

```python
from math import pi

circle = Circle(5)

print(circle.getArea())       # Output: 79
print(circle.getPerimeter())  # Output: 31
```

🚀 Example Usage
```python
circle = Circle(5)

print(circle.getArea())       # Output: 79
print(circle.getPerimeter())  # Output: 31
```

You can change the radius to calculate different values:

```python
circle = Circle(10)
print(circle.getArea())       # Output: 314
print(circle.getPerimeter())  # Output: 63
```

📐 Math Reference
Area = π × radius²

Perimeter = 2 × π × radius

π is imported from Python's built-in math module (math.pi)

Both results are returned as rounded integers for simplicity.

✅ Requirements
Python 3.x

No external libraries required (uses math module)

