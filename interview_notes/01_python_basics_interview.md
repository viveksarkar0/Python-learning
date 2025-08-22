# 🐍 Python Basics - Interview Questions & Answers

## 📋 Table of Contents
1. [Variables & Data Types](#variables--data-types)
2. [Strings](#strings)
3. [Numbers & Math](#numbers--math)
4. [Input/Output](#inputoutput)
5. [Common Interview Questions](#common-interview-questions)

---

## 🔤 Variables & Data Types

### Q1: What are the basic data types in Python?
**Answer:**
```python
# Basic data types
integer = 42          # int
float_num = 3.14      # float
string = "Hello"      # str
boolean = True        # bool
complex_num = 3+4j    # complex
```

**🔥 Interview Tip:** Python is dynamically typed, meaning you don't need to declare variable types.

### Q2: What is the difference between `is` and `==`?
**Answer:**
```python
# == compares values
# is compares object identity (memory location)

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (same values)
print(a is b)  # False (different objects)

# But for small integers, Python caches them
x = 256
y = 256
print(x is y)  # True (cached)
```

### Q3: What is the difference between `list` and `tuple`?
**Answer:**
```python
# Lists are mutable, tuples are immutable
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 10    # ✅ Works
# my_tuple[0] = 10 # ❌ TypeError

# Tuples are faster and use less memory
# Lists are more flexible
```

---

## 📝 Strings

### Q4: How do you reverse a string in Python?
**Answer:**
```python
# Method 1: Slicing
text = "Hello"
reversed_text = text[::-1]  # "olleH"

# Method 2: Using reversed()
reversed_text = ''.join(reversed(text))

# Method 3: Manual loop
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
```

### Q5: What are f-strings and when to use them?
**Answer:**
```python
name = "Vivek"
age = 22

# f-strings (Python 3.6+)
message = f"My name is {name} and I'm {age} years old"

# Old methods
message = "My name is {} and I'm {} years old".format(name, age)
message = "My name is %s and I'm %d years old" % (name, age)
```

**🔥 Interview Tip:** f-strings are more readable and faster than other string formatting methods.

---

## 🔢 Numbers & Math

### Q6: What is the difference between `/` and `//`?
**Answer:**
```python
# / is true division (returns float)
result = 10 / 3    # 3.3333333333333335

# // is floor division (returns integer)
result = 10 // 3   # 3

# % is modulo (remainder)
remainder = 10 % 3 # 1
```

### Q7: How do you handle large numbers in Python?
**Answer:**
```python
# Python automatically handles large integers
large_num = 2**1000
print(large_num)  # No overflow!

# For scientific notation
scientific = 1.23e-4  # 0.000123
```

---

## 📥 Input/Output

### Q8: How do you read user input safely?
**Answer:**
```python
# Basic input
name = input("Enter your name: ")

# Type conversion with error handling
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")
    age = 0

# Input validation
while True:
    try:
        number = int(input("Enter a number (1-10): "))
        if 1 <= number <= 10:
            break
        else:
            print("Number must be between 1 and 10")
    except ValueError:
        print("Please enter a valid number")
```

---

## 🎯 Common Interview Questions

### Q9: What is the difference between `range()` and `xrange()`?
**Answer:**
```python
# In Python 2:
# range() returns a list
# xrange() returns an iterator (memory efficient)

# In Python 3:
# range() returns an iterator (like xrange in Python 2)
# xrange() doesn't exist

# Memory efficient
for i in range(1000000):  # Doesn't create a list in memory
    pass
```

### Q10: What is the difference between `__str__` and `__repr__`?
**Answer:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Vivek", 22)
print(str(person))    # Vivek (22)
print(repr(person))   # Person('Vivek', 22)
```

**🔥 Interview Tip:** `__str__` is for end users, `__repr__` is for developers.

---

## ⚡ Performance Tips

1. **Use list comprehensions** instead of loops when possible
2. **Use `set`** for membership testing (O(1) vs O(n))
3. **Use `join()`** for string concatenation
4. **Use `enumerate()`** when you need both index and value
5. **Use `zip()`** to iterate over multiple sequences

---

## 🎓 Key Takeaways

- ✅ Python is dynamically typed
- ✅ Everything is an object in Python
- ✅ Use meaningful variable names
- ✅ Follow PEP 8 style guide
- ✅ Write readable, maintainable code

---

**Next: [Data Structures Interview Questions](./02_data_structures_interview.md)**
