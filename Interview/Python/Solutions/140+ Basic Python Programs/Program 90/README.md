
# 📧 Program 90: Extract Username from Email Address

This Python program extracts and prints the **username** from a given email address in the format `username@companyname.com`. The email address is assumed to be in the form `username@companyname.com (mailto:username@companyname.com)`.

---

## 📌 Problem Statement

Write a Python program to extract the **username** from a given email address. The email address will be in the format `username@companyname.com` and the username and company names are composed only of letters.

---

## 🧠 Concepts Used

- String manipulation
- `split()` function
- Regular expressions (optional)

---

## 🧪 Sample Code

```python
def extract_username(email):
    # Split the email at '@' and return the first part as username
    return email.split('@')[0]

# Input from user
email = input("Enter the email address: ")

# Extract and print the username
username = extract_username(email)
print(username)
```

---

## 🎯 Example Input & Output

### Input

```
Enter the email address: john@google.com (mailto:john@google.com)
```

### Output

```
john
```

---

## ✅ Notes

- The program splits the email address at the `@` character, and the first part of the split result is the username.
- The solution assumes the email format is consistent and contains only letters for both the username and company name.

---
