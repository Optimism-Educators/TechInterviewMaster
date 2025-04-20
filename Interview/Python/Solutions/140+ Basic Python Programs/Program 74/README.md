# Program74
Here is **Program 74** in the requested format:

---

```markdown
# 📝 Program 74: Calculate and Print Value According to Formula

This Python program calculates and prints the values based on the given formula. The program uses fixed values for `C` and `H`, and for the variable `D`, which is a sequence of numbers inputted by the user.

---

## 📌 Problem Statement

**Write a Python program that calculates and prints the value according to the given formula:**

- **Formula:** 
  \[
  Q = \sqrt{\frac{(D \cdot 2)}{C} - H}
  \]

Where:
- **C** is a fixed constant value: 50.
- **H** is a fixed constant value: 30.
- **D** is the variable whose values are given as a comma-separated sequence.

For example:
- Input: `100,150,180`
- Output: `18,22,24`

---

## 💡 Explanation

1. **Fixed Values**:
   - C = 50
   - H = 30
2. **Formula**:
   - For each value of `D`, calculate:
     \[
     Q = \sqrt{\frac{(D \cdot 2)}{C} - H}
     \]
   - This formula computes the value `Q` based on the given value of `D`.

3. **Input/Output**:
   - Input: A comma-separated string of numbers (e.g., `100,150,180`).
   - Output: A comma-separated string of results.

---

## ✅ Sample Code

```python
import math

# Constants
C = 50
H = 30

# Function to calculate Q
def calculate_q(D):
    return int(math.sqrt((2 * D) / C - H))

# Input sequence of D values as a comma-separated string
input_values = input("Enter the values of D (comma-separated): ")

# Convert the input string to a list of integers
D_values = [int(d) for d in input_values.split(',')]

# Calculate and store the results
results = [calculate_q(D) for D in D_values]

# Print the output
print("The output values are:", ','.join(map(str, results)))
```

---

## ▶️ Example Output

```bash
Enter the values of D (comma-separated): 100,150,180
The output values are: 18,22,24
```

---

## 🔍 Explanation

1. **Constants C and H**:
   - These are set to 50 and 30, respectively, as per the problem statement.

2. **Input**:
   - The user is prompted to enter values for `D` as a comma-separated sequence.

3. **Calculation**:
   - For each value in the input sequence, the program applies the formula to calculate the corresponding value of `Q`:
     \[
     Q = \sqrt{\frac{(D \cdot 2)}{C} - H}
     \]

4. **Output**:
   - The program calculates and displays the results as a comma-separated string.

---

## 🎯 Use Case

This type of calculation can be useful in various scientific and engineering applications where specific formulas need to be applied to a series of values.

---

Let me know if you'd like further clarification or any adjustments to the program! 😊

```

---

Feel free to ask if you need further modifications!
