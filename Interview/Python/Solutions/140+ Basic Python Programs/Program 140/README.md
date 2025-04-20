
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

---
--

### 🧠 Function Logic

- **vow_replace(input_string, replacement_vowel)**:
  - The function takes two arguments:
    - `input_string`: A string where vowels need to be replaced.
    - `replacement_vowel`: A single vowel character that will replace all the vowels in the string.
  - The function will:
    - Identify all the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) in the string.
    - Replace each vowel with the specified replacement vowel.
    - Return the modified string.

### 🧠 Example Walkthrough
```python
def vow_replace(input_string, replacement_vowel):
    vowels = ['a', 'e', 'i', 'o', 'u']
    modified_string = ""
    for char in input_string:
        if char in vowels:
            modified_string += replacement_vowel
        else:
            modified_string += char
    return modified_string

# Example usage
print(vow_replace("apples and bananas", "u"))  # Output: "upplus und bununus"
print(vow_replace("cheese casserole", "o"))    # Output: "chooso cossorolo"
print(vow_replace("stuffed jalapeno poppers", "e"))  # Output: "steffed jelepene peppers"
```

--- 

### 📖 Function Documentation

```python
def vow_replace(input_string, replacement_vowel):
    """
    Replace all vowels in the input_string with the replacement_vowel.

    Parameters:
    - input_string (str): The string to be modified.
    - replacement_vowel (str): The single vowel character to replace all vowels.

    Returns:
    - str: The modified string with vowels replaced by the replacement vowel.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    modified_string = ""
    for char in input_string:
        if char in vowels:
            modified_string += replacement_vowel
        else:
          modified_string += char
    return modified_string
```

### 📖 Function Details

- **Function Name**: `vow_replace`
- **Parameters**:
  - `input_string` (str): The string to be modified.
  - `replacement_vowel` (str): The single vowel character to replace all vowels.
- **Return Value**: The modified string with vowels replaced by the replacement vowel.
- **Function Logic**:
  - The function iterates through each character in the input string.
  - If the character is a vowel, it replaces it with the specified replacement vowel.
  - Otherwise, it keeps the character as it is.
  - The modified string is then returned.



### 📖 Function Benefits

- **Efficiency**: The function operates in linear time complexity, making it efficient for strings of any length.
- **Modifiability**: The function is straightforward and easy to modify if the requirement changes.
- **Reusability**: The function can be reused in different contexts by changing the replacement vowel.

### 📖 Function Limitations

- **Case Sensitivity**: The function is case-insensitive, treating uppercase and lowercase vowels as the same.
- **Vowel Replacement**: The function only replaces vowels with the specified replacement vowel. Other characters remain unchanged.
- **Vowel Set**: The function assumes that the vowels to be replaced are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### 📖 Function Code

```python
def vow_replace(input_string, replacement_vowel):
    vowels = 'aeiou'
    modified_string = ''
    for char in input_string:
        if char in vowels:
            modified_string += replacement_vowel
        else:
            modified_string += char
    return modified_string
```

### 📖 Function Complexity

- **Time Complexity**: O(n), where n is the length of the input string.
- **Space Complexity**: O(n), as the function creates a new string to store the modified characters.

### 📖 Function Dependencies

- **None**

### 📖 Function Additional Information

- **Vowel Set**: The function assumes that the vowels to be replaced are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
- **Case Sensitivity**: The function is case-insensitive, treating uppercase and lowercase vowels as the same.
- **Vowel Replacement**: The function only replaces vowels with the specified replacement vowel. Other characters remain unchanged.
- **Modifiability**: The function is straightforward and easy to modify if the requirement changes.
- **Reusability**: The function can be reused in different contexts by changing the replacement vowel.
- **Efficiency**: The function operates in linear time complexity, making it efficient for strings of any length.

### 📖 Function Usage

- **Example 1**:  
  ```python
  print(vow_replace("apples and bananas", "u"))
  # Output: "upplus und bununus"
  ```

- **Example 2**:
  ```python
  print(vow_replace("cheese casserole", "o"))
  # Output: "chooso cossorolo"
  ```

- **Example 3**:
  ```python
  print(vow_replace("stuffed jalapeno poppers", "e"))
  # Output: "steffed jelepene peppers"
  ```

### 📖 Function Conclusion

This function provides a simple yet effective way to replace vowels in a string with a specified vowel. It's a fundamental operation in text processing and can be applied in various scenarios where vowel replacement is required.
