Here is the **README.md** file for **Program 141 – ASCII Capitalization**:

---

## 📘 Program 141 – ASCII Capitalization

### 📝 Description  

This program defines a function `ascii_capitalize()` that takes a string as input and capitalizes a letter if its ASCII code is even, while converting it to lowercase if its ASCII code is odd. This function examines each character in the string and adjusts its case based on its ASCII code.

### ✅ Examples

```python
ascii_capitalize("to be or not to be!")
# ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID")
# ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.")
# ➞ "oH wHaT a BeauTiFuL moRNiNg."
```

---

### 🧠 Function Logic

- **ascii_capitalize(input_string)**:
  - The function takes one argument:
    - `input_string`: The string in which characters' cases will be modified.
  - The function iterates through each character in the string, checks its ASCII code using the `ord()` function, and:
    - Capitalizes the character if its ASCII code is even.
    - Converts it to lowercase if its ASCII code is odd.
  - It then returns the modified string with appropriate capitalizations.

---

### 🧠 Function Definition

```python
def ascii_capitalize(input_string):
    # Iterate through each character in the string and apply the condition
    return ''.join([char.upper() if ord(char) % 2 == 0 else char.lower() for char in input_string])
```

---

### 🔁 How to Use

1. Provide a string `input_string` which may contain any characters.
2. The function will iterate over each character, checking its ASCII value and modify its case accordingly.
3. The result will be a new string where characters with even ASCII values are capitalized, and those with odd ASCII values are in lowercase.

### 💡 Example Usage

```python
# Input string
input_string = "to be or not to be!"

# Call the function
result = ascii_capitalize(input_string)

# Output the result
print(result)  # Output: "To Be oR NoT To Be!"
```

---

### 🧠 Example Walkthrough

For the input `"to be or not to be!"`:

- The function evaluates each character:
  - For `"t"`, the ASCII code is 116 (even), so it is capitalized to `"T"`.
  - For `"o"`, the ASCII code is 111 (odd), so it is converted to `"o"`.
  - The same logic is applied for the rest of the string, resulting in `"To Be oR NoT To Be!"`.

For the input `"THE LITTLE MERMAID"`:

- The function evaluates each character:
  - `"T"` (ASCII 84) is even, so it remains `"T"`.
  - `"H"` (ASCII 72) is even, so it remains `"H"`.
  - And so on for the rest of the characters, resulting in `"THe LiTTLe meRmaiD"`.

For the input `"Oh what a beautiful morning."`:

- The same process occurs, and the output is `"oH wHaT a BeauTiFuL moRNiNg."`.

---

### 🧠 Additional Notes

- The `ord()` function is used to retrieve the ASCII value of each character.
- This solution works with any printable characters and will modify only the alphabetic characters based on their ASCII values.
- Non-alphabetic characters (such as spaces, punctuation marks, etc.) remain unchanged.

---

### 🔍 Example Input/Output

- **Input**: `"to be or not to be!"`
  - **Output**: `"To Be oR NoT To Be!"`

- **Input**: `"THE LITTLE MERMAID"`
  - **Output**: `"THe LiTTLe meRmaiD"`

- **Input**: `"Oh what a beautiful morning."`
  - **Output**: `"oH wHaT a BeauTiFuL moRNiNg."`

---

Let me know if you need any further modifications or details!
