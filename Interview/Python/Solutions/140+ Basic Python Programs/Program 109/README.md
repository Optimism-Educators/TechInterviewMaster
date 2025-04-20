
# 📘 Program 109: Calculate the Thickness of a Paper After Folding

## 🧮 Description

This Python program defines a function that calculates the thickness of a piece of paper after folding it `n` number of times. The paper starts off with an initial thickness of 0.5mm. The function calculates the thickness after each fold and converts the final thickness into meters.

### Formula:
For each fold, the thickness of the paper doubles. The formula to calculate the thickness is:

- Initial thickness = 0.5mm
- After `n` folds: Thickness = `0.5 * 2^n` mm
- Convert the final thickness from millimeters to meters by dividing by 1000.

---

## 📌 Function Definition

```python
def num_layers(n):
    thickness_mm = 0.5 * (2 ** n)  # Calculate thickness in mm after n folds
    thickness_m = thickness_mm / 1000  # Convert mm to meters
    return f"{thickness_m}m"  # Return the result as a string in meters
```

---

## ✅ Examples

```python
print(num_layers(1))    # ➞ "0.001m"
print(num_layers(4))    # ➞ "0.008m"
print(num_layers(21))   # ➞ "1048.576m"
```

### 💡 Output

```
0.001m
0.008m
1048.576m
```

---

## 📂 Use Cases

- **Understanding Exponential Growth**: This program demonstrates the concept of exponential growth, as the thickness of the paper doubles with each fold.
- **Paper Folding in Real Life**: The program can be used to estimate how thick a folded paper might become after many folds, which is a fun concept in physics and math.
- **Mathematical Calculation Practice**: Helps understand how powers of 2 work and how to apply them in real-world scenarios.

---

## 🛡️ Notes

- The function uses the formula `thickness_mm = 0.5 * (2 ** n)` to calculate the thickness in millimeters.
- It then converts this thickness to meters by dividing by 1000 (`thickness_m = thickness_mm / 1000`).
- The output is formatted as a string with the unit `m` for meters.

---

