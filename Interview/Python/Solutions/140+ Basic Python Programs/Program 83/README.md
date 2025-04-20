# Program83
Absolutely! Here's **Program 83** in your requested format:

---

```markdown
# 👥 Program 83: Person Class with Male and Female Subclasses

This Python program defines a base class `Person` and two subclasses `Male` and `Female`, each with a method `getGender()` that returns the appropriate gender.

---

## 📌 Problem Statement

**Define a class `Person` and its two child classes: `Male` and `Female`.**  
Each class should have a method called `getGender()`.

- For the `Male` class, `getGender()` should return `"Male"`.
- For the `Female` class, `getGender()` should return `"Female"`.

---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Inheritance
- Method Overriding

---

## 🧪 Sample Code

```python
# Define the base class
class Person:
    def getGender(self):
        return "Not Specified"

# Define the Male subclass
class Male(Person):
    def getGender(self):
        return "Male"

# Define the Female subclass
class Female(Person):
    def getGender(self):
        return "Female"

# Create objects
person1 = Male()
person2 = Female()

# Print gender using getGender method
print(person1.getGender())  # Output: Male
print(person2.getGender())  # Output: Female
```

---

## 🎯 Output

```
Male  
Female
```

---

## 🧠 Notes

- This is a simple demonstration of **inheritance** and **polymorphism**.
- The `getGender()` method is **overridden** in the child classes to provide specific behavior.

---
