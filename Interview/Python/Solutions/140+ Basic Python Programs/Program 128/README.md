# Program128
A simple Python class that takes a string of comma-separated integers and computes their product.

---

## 📌 Description

The `NumberStringMultiplier` class allows you to input a string of integers separated by commas (and optional spaces), parse them, and compute their product.

This is useful when dealing with user input or data coming from text sources where numbers are stored as a single string.

---

## 🧩 Class Definition

```python
class NumberStringMultiplier:
    def __init__(self, number_string):
        self.number_string = number_string

    def getProduct(self):
        try:
            numbers = [int(num.strip()) for num in self.number_string.split(",")]
            product = 1
            for num in numbers:
                product *= num
            return product
        except ValueError:
            raise ValueError("Not valid string. Must contains int numbers separated from comma and spaces.")
```

🧪 Example Usage

```python
# Create an instance
multiplier = NumberStringMultiplier("2, 3, 4")

# Get the product of the numbers
result = multiplier.getProduct()

print(result)  # Output: 24
```

⚠️ Error Handling
If the input string contains non-integer values, a ValueError will be raised:

```python
multiplier = NumberStringMultiplier("2, three, 4")
result = multiplier.getProduct()
# Raises: ValueError: Not valid string. Must contains int numbers separated from comma and spaces.
```
✅ Input Format
The input string must:

Contain integers only

Use commas (,) as separators

Allow optional spaces

Valid examples:

"1,2,3"

"4, 5, 6"

Invalid examples:

"1;2;3"

"a, b, c"

"10, twenty"

