# Program91
Here’s **Program 91** written in the format you prefer:

---

```markdown
# 🟩 Program 91: Define Shape Class and its Subclass Square

This Python program defines a base class **Shape** and its subclass **Square**. The **Square** class has an `__init__` function that takes the side length as an argument. Both classes have an `area` method that calculates and prints the area of the shape. By default, the area for **Shape** is set to 0.

---

## 📌 Problem Statement

Define a class **Shape** with an `area` method. Then define a subclass **Square**, which takes a side length as an argument and overrides the `area` method to calculate the area of the square. The area of a general shape is assumed to be 0 by default.

---

## 🧠 Concepts Used

- Inheritance
- Method Overriding
- Class and Instance variables
- Constructor (`__init__`)

---

## 🧪 Sample Code

```python
# Define the base class Shape
class Shape:
    def area(self):
        return 0  # Default area for general shape is 0

# Define the subclass Square
class Square(Shape):
    def __init__(self, length):
        self.length = length  # Initialize the length of the square's side

    # Override the area method to calculate square's area
    def area(self):
        return self.length ** 2  # Area of a square: side^2

# Example usage
shape = Shape()  # Create an object of Shape
print(f"Shape area: {shape.area()}")  # Output: 0 (default)

square = Square(5)  # Create an object of Square with side length 5
print(f"Square area: {square.area()}")  # Output: 25 (5^2)
```

---

## 🎯 Example Input & Output

### Input

```
(No input required; output is based on class behavior.)
```

### Output

```
Shape area: 0
Square area: 25
```

---

## ✅ Notes

- The `Shape` class defines a default `area` method, which returns 0.
- The `Square` class inherits from `Shape` and overrides the `area` method to calculate the area of a square.
- The `Square` class uses the formula **side²** to calculate the area of the square.

---

Let me know if you need further modifications! 🌟

```
