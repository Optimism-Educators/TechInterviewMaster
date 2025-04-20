# Program120
Here's the **README.md** file for **Program 120 – Compound Interest Calculation**:

---

## 📘 Program 120 – Compound Interest Calculation

### 📝 Description  

This program defines a function `compound_interest(p, t, r, n)` that calculates the value of an investment at the end of a specified term, using compound interest. The function takes in four parameters:

- **p**: Principal amount (initial investment)
- **t**: Time period of the investment in years
- **r**: Annual interest rate (expressed as a decimal)
- **n**: Number of compounding periods per year (monthly = 12, annually = 1, etc.)

The function then returns the final value of the investment after the specified time period, rounded to the nearest cent.

### 🌱 Formula

The formula for compound interest is:
\[
A = P \left(1 + \frac{r}{n}\right)^{nt}
\]
Where:

- **A** is the amount of money accumulated after n years, including interest.
- **P** is the principal amount (the initial money).
- **r** is the annual interest rate (in decimal form).
- **t** is the number of years the money is invested.
- **n** is the number of times the interest is compounded per year.

---

### ✅ Examples

```python
compound_interest(10000, 10, 0.06, 12) ➞ 18193.97

compound_interest(100, 1, 0.05, 1) ➞ 105.0

compound_interest(3500, 15, 0.1, 4) ➞ 15399.26

compound_interest(100000, 20, 0.15, 365) ➞ 2007316.26
```

---

### 💡 Function Logic

1. **Input**: The user provides the principal amount **p**, the time period **t**, the interest rate **r**, and the number of compounding periods per year **n**.
2. **Formula Application**: The function uses the compound interest formula to compute the accumulated value after the specified number of years.
3. **Return**: The final value of the investment is rounded to two decimal places and returned.

---

### 🧠 Function Definition

```python
def compound_interest(p, t, r, n):
    A = p * (1 + r / n) ** (n * t)
    return round(A, 2)
```

---

### 🔁 How to Use

1. Call the `compound_interest()` function with the following parameters:
   - **p**: Initial investment (Principal amount)
   - **t**: Term in years
   - **r**: Annual interest rate (as a decimal)
   - **n**: Number of compounding periods per year (e.g., 12 for monthly)
2. The function will return the total accumulated value at the end of the term, rounded to the nearest cent.

---

Let me know if you'd like this in `.md` format or included with any other files!
