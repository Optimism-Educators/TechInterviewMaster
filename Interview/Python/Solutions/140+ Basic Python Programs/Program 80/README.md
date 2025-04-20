
# 🔐 Program 80: Password Validation Checker

This Python program checks the validity of passwords based on a set of security criteria commonly required during registration on a website.

---

## 📌 Problem Statement

**Write a Python program to validate a list of user-input passwords based on the following rules:**

### ✅ Password Requirements:

1. Must contain at least **1 lowercase letter** `[a-z]`  
2. Must contain at least **1 uppercase letter** `[A-Z]`  
3. Must contain at least **1 digit** `[0-9]`  
4. Must contain at least **1 special character** from `$#@`  
5. Must be between **6 and 12 characters** long  

---

## 💡 Input Format

- Accept a **comma-separated list** of passwords as input.

### Example Input:
```

ABd1234@1,a F1#,2w3E*,2We3345

```

---

## ✅ Output Format

- Print the **valid passwords**, separated by commas.

### Example Output:
```

ABd1234@1

```

---

## 🧠 Logic

- For each password:
  - Check if all the rules are satisfied.
  - If valid, add it to the output list.

---

## 🧪 Sample Code

```python
import re

# Input comma-separated passwords
passwords = input("Enter comma-separated passwords to validate: ").split(',')

# List to store valid passwords
valid_passwords = []

# Loop through each password
for pwd in passwords:
    if (6 <= len(pwd) <= 12 and
        re.search(r'[a-z]', pwd) and
        re.search(r'[A-Z]', pwd) and
        re.search(r'[0-9]', pwd) and
        re.search(r'[$#@]', pwd)):
        valid_passwords.append(pwd)

# Output valid passwords
print(",".join(valid_passwords))
```

---

## 🎯 Example Execution

```bash
Enter comma-separated passwords to validate: ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1
```

---

## 🔍 Notes

- This is useful for enforcing password policies in web or app development.
- Regular expressions make it easy to validate character presence.

---
