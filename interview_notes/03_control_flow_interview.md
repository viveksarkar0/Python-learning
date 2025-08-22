# 🐍 Python Control Flow - Interview Questions & Answers

## 📋 Table of Contents
1. [Conditional Statements](#conditional-statements)
2. [Loops](#loops)
3. [List Comprehensions](#list-comprehensions)
4. [Error Handling](#error-handling)
5. [Common Interview Questions](#common-interview-questions)

---

## 🔀 Conditional Statements

### Q1: What is the difference between `if`, `elif`, and `else`?
**Answer:**
```python
# if: First condition to check
# elif: Additional conditions (only if previous conditions are False)
# else: Default case (only if all conditions are False)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)  # "B"
```

**🔥 Interview Tip:** `elif` is more efficient than multiple `if` statements because it stops checking once a condition is True.

### Q2: What is the ternary operator in Python?
**Answer:**
```python
# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (conditional expression)
status = "adult" if age >= 18 else "minor"

# Multiple conditions
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

### Q3: How do you check multiple conditions?
**Answer:**
```python
# Using and, or, not
age = 25
income = 50000

# All conditions must be True
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# At least one condition must be True
if age >= 65 or income >= 100000:
    print("Eligible for discount")

# Using parentheses for complex logic
if (age >= 18 and income >= 30000) or (age >= 65):
    print("Eligible")

# Using in for multiple values
grade = "A"
if grade in ["A", "B", "C"]:
    print("Passing grade")
```

---

## 🔄 Loops

### Q4: What are the different types of loops in Python?
**Answer:**
```python
# 1. for loop (iterate over sequences)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over dictionary
person = {"name": "Vivek", "age": 22}
for key, value in person.items():
    print(f"{key}: {value}")

# 2. while loop (repeat while condition is True)
count = 0
while count < 5:
    print(count)
    count += 1

# 3. Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### Q5: What is the difference between `break`, `continue`, and `pass`?
**Answer:**
```python
# break: Exit the loop completely
for i in range(10):
    if i == 5:
        break  # Stop at 5
    print(i)  # 0, 1, 2, 3, 4

# continue: Skip current iteration, continue with next
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # 1, 3, 5, 7, 9

# pass: Do nothing (placeholder)
for i in range(10):
    if i < 5:
        pass  # Do nothing for i < 5
    else:
        print(i)  # 5, 6, 7, 8, 9
```

### Q6: How do you use `enumerate()` in loops?
**Answer:**
```python
# enumerate() provides both index and value
fruits = ["apple", "banana", "cherry"]

# Method 1: Using enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Method 2: Start enumeration from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Method 3: Manual approach (not recommended)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

---

## 📝 List Comprehensions

### Q7: What are list comprehensions and when to use them?
**Answer:**
```python
# Basic list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Nested list comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_squares = {x**2 for x in range(5)}
print(unique_squares)  # {0, 1, 4, 9, 16}
```

### Q8: When should you avoid list comprehensions?
**Answer:**
```python
# Avoid when:
# 1. Logic is complex
# 2. Multiple operations are needed
# 3. Readability is important

# ❌ Complex logic (hard to read)
result = [x**2 if x % 2 == 0 else x**3 for x in range(10) if x > 0 and x < 8]

# ✅ Better with regular loop
result = []
for x in range(10):
    if x > 0 and x < 8:
        if x % 2 == 0:
            result.append(x**2)
        else:
            result.append(x**3)

# ❌ Multiple operations
data = [process_item(item) for item in items if validate_item(item)]

# ✅ Better with regular loop
data = []
for item in items:
    if validate_item(item):
        processed = process_item(item)
        data.append(processed)
```

---

## ⚠️ Error Handling

### Q9: How do you handle exceptions in Python?
**Answer:**
```python
# Basic try-except
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")

# try-except-else-finally
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
finally:
    file.close()  # Always executed

# Using with statement (recommended)
try:
    with open("data.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
```

### Q10: How do you raise custom exceptions?
**Answer:**
```python
# Custom exception class
class AgeError(Exception):
    pass

class InvalidAgeError(AgeError):
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Using custom exceptions
def validate_age(age):
    if age < 0:
        raise InvalidAgeError(age, "Age cannot be negative")
    elif age > 150:
        raise InvalidAgeError(age, "Age seems unrealistic")
    return True

# Testing
try:
    validate_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e.message}, Age: {e.age}")
```

---

## 🎯 Common Interview Questions

### Q11: How do you find the factorial of a number?
**Answer:**
```python
# Method 1: Iterative
def factorial_iterative(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Method 2: Recursive
def factorial_recursive(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Method 3: Using math module
import math
def factorial_math(n):
    return math.factorial(n)

print(factorial_iterative(5))  # 120
```

### Q12: How do you check if a number is prime?
**Answer:**
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd numbers up to square root
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(17))  # True
print(is_prime(25))  # False
```

### Q13: How do you reverse a number?
**Answer:**
```python
# Method 1: Using string conversion
def reverse_number_string(n):
    return int(str(n)[::-1])

# Method 2: Mathematical approach
def reverse_number_math(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

print(reverse_number_string(12345))  # 54321
print(reverse_number_math(12345))    # 54321
```

---

## ⚡ Performance Tips

1. **Use `range()` instead of `xrange()`** (Python 3)
2. **Use list comprehensions** for simple operations
3. **Use `enumerate()`** instead of manual indexing
4. **Use `zip()`** to iterate over multiple sequences
5. **Use `break` early** to exit loops when possible

---

## 🎓 Key Takeaways

- ✅ Use `elif` for multiple conditions (more efficient)
- ✅ List comprehensions are faster than loops for simple operations
- ✅ Always handle exceptions appropriately
- ✅ Use `with` statement for file operations
- ✅ Choose the right loop type for your use case

---

**Next: [Functions Interview Questions](./04_functions_interview.md)**
