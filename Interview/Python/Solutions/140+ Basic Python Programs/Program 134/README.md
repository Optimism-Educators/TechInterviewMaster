# Program134
Here is the **README.md** file for **Program 134 – Circle Class Constructor**:

---

## 📘 Program 134 – Circle Class Constructor

### 📝 Description  

This program defines a `Circle` class that constructs a circle with a given radius. The class includes two methods:

1. `getArea()`: Returns the area of the circle (calculated using the formula \( \pi r^2 \)).
2. `getPerimeter()`: Returns the perimeter (circumference) of the circle (calculated using the formula \( 2 \pi r \)).

The radius of the circle is passed as an argument when creating an instance of the `Circle` class. The results for the area and perimeter are rounded to the nearest integer.

---

### ✅ Examples

```python
circy = Circle(11)
print(circy.getArea())        # ➞ 380
print(circy.getPerimeter())   # ➞ 69

circy = Circle(4.44)
print(circy.getArea())        # ➞ 62
print(circy.getPerimeter())   # ➞ 27
```

---

### 🧠 Function Logic

1. **Constructor**:
   - Accepts a radius as input when an object is created.

2. **getArea()**:
   - Calculates the area of the circle using the formula:
     \[
     \text{Area} = \pi \times r^2
     \]
   - The result is rounded to the nearest integer.

3. **getPerimeter()**:
   - Calculates the perimeter (circumference) of the circle using the formula:
     \[
     \text{Perimeter} = 2 \pi \times r
     \]
   - The result is rounded to the nearest integer.

---

### 🧠 Class Definition

```python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        # Calculate and return the area of the circle
        return round(math.pi * self.radius ** 2)
    
    def getPerimeter(self):
        # Calculate and return the perimeter (circumference) of the circle
        return round(2 * math.pi * self.radius)
```

---

### 🔁 How to Use

1. Instantiate the `Circle` class by passing the desired radius as an argument.
2. Call the `getArea()` method on the instance to get the area of the circle.
3. Call the `getPerimeter()` method on the instance to get the perimeter (circumference) of the circle.

### 💡 Example Usage

```python
# Creating a Circle object with radius 11
circy = Circle(11)

# Getting the area
print(circy.getArea())        # Output: 380

# Getting the perimeter
print(circy.getPerimeter())   # Output: 69
```

---

### 🧠 Example Walkthrough

For the input `Circle(11)`:

- **getArea()**:  
  \[
  \text{Area} = \pi \times 11^2 = \pi \times 121 \approx 380.132711084365
  \]
  After rounding to the nearest integer, the result is `380`.

- **getPerimeter()**:  
  \[
  \text{Perimeter} = 2 \pi \times 11 = 69.11503837847544
  \]
  After rounding to the nearest integer, the result is `69`.

For the input `Circle(4.44)`:

- **getArea()**:  
  \[
  \text{Area} = \pi \times 4.44^2 = \pi \times 19.7136 \approx 62.00717843222079
  \]
  After rounding to the nearest integer, the result is `62`.

- **getPerimeter()**:  
  \[
  \text{Perimeter} = 2 \pi \times 4.44 = 27.897342763877365
  \]
  After rounding to the nearest integer, the result is `28`.

---

### 🧠 Additional Notes

- The `getArea()` and `getPerimeter()` methods round the results to the nearest integer.
- This program assumes the radius provided is a positive number.

---

### 🔍 Example Input/Output

- **Input**: `Circle(11)`
  - **Output**:
    - `Area: 380`
    - `Perimeter: 69`

- **Input**: `Circle(4.44)`
  - **Output**:
    - `Area: 62`
    - `Perimeter: 28`

---

Let me know if you need any further modifications!
