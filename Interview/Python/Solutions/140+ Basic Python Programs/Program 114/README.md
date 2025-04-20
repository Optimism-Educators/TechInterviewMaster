
## 📘 Program 114 - Cone Volume Calculator

### 🔍 Description  

This program defines a function that calculates the **volume of a cone** using the provided height and radius. The result is **rounded to the nearest hundredth (2 decimal places)**.

The formula to compute the volume of a cone is:
\[
V = \frac{1}{3} \pi r^2 h
\]
Where:  

- \( r \) is the radius of the cone base  
- \( h \) is the height of the cone  
- \( \pi \approx 3.14159 \)

---

### 🧠 Function Signature

```python
def cone_volume(h, r):
```

---

### 🧮 Parameters  

- `h` (float or int): Height of the cone  
- `r` (float or int): Radius of the base of the cone

---

### 🚀 Returns  

- `float`: Volume of the cone, rounded to two decimal places.

---

### ✅ Examples

```python
cone_volume(3, 2) ➞ 12.57  
cone_volume(15, 6) ➞ 565.49  
cone_volume(18, 0) ➞ 0.0
```

---

### 🧪 Sample Code

```python
import math

def cone_volume(h, r):
    volume = (1/3) * math.pi * r**2 * h
    return round(volume, 2)

# Example usage
print(cone_volume(3, 2))    # ➞ 12.57
print(cone_volume(15, 6))   # ➞ 565.49
print(cone_volume(18, 0))   # ➞ 0.0
```

---

### 📌 Notes

- The `math` module is used to access an accurate value of π (`math.pi`).
- If the radius is 0, the volume is also 0.
- You can change the precision by adjusting the `round()` function.
