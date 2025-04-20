# Program81
Absolutely! Here's **Program 81** in your preferred style and formatting:

---

```markdown
# 🔢 Program 81: Generator Class to Yield Numbers Divisible by 7

This Python program defines a class that includes a generator function to iterate over numbers divisible by 7 in a given range from `0` to `n`.

---

## 📌 Problem Statement

**Define a class with a generator function that yields numbers divisible by 7, from 0 up to a given number `n` (inclusive).**

---

## 💡 Input Format

- A single integer `n`, which defines the upper limit of the range.

### Example Input:
```

50

```

---

## ✅ Output Format

- Numbers divisible by 7 from 0 to `n`, printed one per line (or as desired).

### Example Output:
```

0
7
14
21
28
35
42
49

```

---

## 🧠 Logic

- Create a class `DivisibleBySeven`.
- Define a generator method `divisible_numbers(self, n)` inside the class.
- Use a loop to yield numbers divisible by 7 in the range `0` to `n`.

---

## 🧪 Sample Code

```python
class DivisibleBySeven:
    def divisible_numbers(self, n):
        for i in range(0, n + 1):
            if i % 7 == 0:
                yield i

# Input the upper limit
n = int(input("Enter the upper limit (n): "))

# Create an instance of the class
generator_obj = DivisibleBySeven()

# Use the generator and print results
print(f"Numbers divisible by 7 from 0 to {n}:")
for num in generator_obj.divisible_numbers(n):
    print(num)
```

---

## 🎯 Example Execution

```bash
Enter the upper limit (n): 50
Numbers divisible by 7 from 0 to 50:
0
7
14
21
28
35
42
49
```

---

## 🔍 Notes

- This demonstrates how to use Python classes and generators together.
- Generators are memory-efficient because they yield values one at a time.

---

Let me know if you want Program 82 next or want all these formatted into a single notebook or document! 🧾

```

---
