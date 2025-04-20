
## 📘 Program 140 – Replace Vowels in a String

### 📝 Description  

This program defines a function `vow_replace()` that takes a string and replaces all vowels in the string with a specified vowel. The vowels to be replaced are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`. The function operates under the assumption that all words in the string are in lowercase and the letter `'y'` is not considered a vowel.

### ✅ Examples

```python
vow_replace("apples and bananas", "u")
# ➞ "upplus und bununus"

vow_replace("cheese casserole", "o")
# ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e")
# ➞ "steffed jelepene peppers"
```

---

### 🧠 Function Logic

- **vow_replace(input_string, replacement_vowel)**:
  - The function takes two arguments:
    - `input_string`: A string where vowels need to be replaced.
    - `replacement_vowel`: A single vowel character that will replace all the vowels in the string.
  - The function will:
    - Identify all the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) in the string.
    - Replace every vowel with the specified `replacement_vowel`.

---

### 🧠 Function Definition

```python
def vow_replace(input_string, replacement_vowel):
    # Define the vowels to replace
    vowels = "aeiou"
    
    # Use string comprehension to replace vowels with the replacement vowel
    return ''.join([replacement_vowel if char in vowels else char for char in input_string])
```

---

### 🔁 How to Use

1. Provide a string `input_string` where vowels need to be replaced.
2. Specify the `replacement_vowel` (a single vowel character).
3. The function will return a new string with all vowels replaced by the specified vowel.

### 💡 Example Usage

```python
# Input string and replacement vowel
input_string = "apples and bananas"
replacement_vowel = "u"

# Call the function
result = vow_replace(input_string, replacement_vowel)

# Output the result
print(result)  # Output: "upplus und bununus"
```

---

### 🧠 Example Walkthrough

For the input `"apples and bananas"` and the replacement vowel `"u"`:

- The vowels `'a'` and `'e'` in the string will be replaced by `'u'`, resulting in the output `"upplus und bununus"`.

For the input `"cheese casserole"` and the replacement vowel `"o"`:

- The vowels `'e'` will be replaced by `'o'`, resulting in the output `"chooso cossorolo"`.

For the input `"stuffed jalapeno poppers"` and the replacement vowel `"e"`:

- The vowels `'u'`, `'a'`, `'o'` in the string will be replaced by `'e'`, resulting in the output `"steffed jelepene peppers"`.

---

### 🧠 Additional Notes

- All words in the input string are assumed to be lowercase.
- The letter `'y'` is not considered a vowel and will not be replaced.
- The function works efficiently for strings of any length.

---

### 🔍 Example Input/Output

- **Input**: `"apples and bananas"`, `"u"`
  - **Output**: `"upplus und bununus"`

- **Input**: `"cheese casserole"`, `"o"`
  - **Output**: `"chooso cossorolo"`

- **Input**: `"stuffed jalapeno poppers"`, `"e"`
  - **Output**: `"steffed jelepene peppers"`

