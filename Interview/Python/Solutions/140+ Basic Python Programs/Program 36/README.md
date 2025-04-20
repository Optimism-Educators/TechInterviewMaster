
# 📈 Program 36: Check if a Given Array is Monotonic

This Python program checks whether a given array is **monotonic**, meaning that the elements are either entirely **non-increasing** or **non-decreasing**.

---

## 📌 Problem Statement

**Write a Python program to check if a given array is monotonic.**

---

## ℹ️ What is a Monotonic Array?

An array is called **monotonic** if it is either:
- **Monotonically increasing**: Each element is greater than or equal to the previous element.
- **Monotonically decreasing**: Each element is less than or equal to the previous element.

### ✅ Examples

- `[1, 2, 2, 3]` → **Monotonic increasing**
- `[6, 5, 4, 4]` → **Monotonic decreasing**
- `[1, 3, 2]` → **Not monotonic**

---

## ✅ Sample Code

```python
# Function to check if array is monotonic
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

# Input from user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

# Check monotonicity
if is_monotonic(arr):
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")
```

---

## ▶️ Example Output

```bash
Enter the array elements separated by space: 1 2 2 3
The array is monotonic.

Enter the array elements separated by space: 5 4 2 2 1
The array is monotonic.

Enter the array elements separated by space: 1 3 2
The array is not monotonic.
```

---

## 📁 Suggested Project Structure

```
monotonic_array_check/
├── is_monotonic.py
└── README.md
```

---

## 💡 Challenge Yourself

- Extend this program to check **strictly increasing or decreasing** sequences.
- Allow checking for **monotonic subsequences**.
- Implement for **floating point** arrays.

