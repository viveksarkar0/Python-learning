# 🐍 Python Functions - Interview Questions & Answers

## 📋 Table of Contents
1. [Function Basics](#function-basics)
2. [Parameters and Arguments](#parameters-and-arguments)
3. [Return Values](#return-values)
4. [Scope and Namespaces](#scope-and-namespaces)
5. [Lambda Functions](#lambda-functions)
6. [Decorators](#decorators)
7. [Common Interview Questions](#common-interview-questions)

---

## 🔧 Function Basics

### Q1: What is a function and why use them?
**Answer:**
```python
# Function: A reusable block of code that performs a specific task
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

# Benefits:
# 1. Reusability - write once, use many times
# 2. Modularity - break code into smaller parts
# 3. Readability - code is easier to understand
# 4. Maintainability - easier to update and fix

# Usage
print(greet("Vivek"))  # Hello, Vivek!
print(greet("Alice"))  # Hello, Alice!
```

### Q2: What is the difference between `def` and `lambda`?
**Answer:**
```python
# def: Regular function definition
def square(x):
    return x ** 2

# lambda: Anonymous function (one-liner)
square_lambda = lambda x: x ** 2

# Both do the same thing
print(square(5))        # 25
print(square_lambda(5)) # 25

# lambda is useful for simple operations
# def is better for complex logic
```

---

## 📥 Parameters and Arguments

### Q3: What are the different types of parameters?
**Answer:**
```python
# 1. Positional parameters
def add(a, b):
    return a + b

# 2. Default parameters
def greet(name="Guest"):
    return f"Hello, {name}!"

# 3. Keyword arguments
def person_info(name, age, city):
    return f"{name} is {age} years old from {city}"

# 4. Variable-length arguments (*args)
def sum_all(*args):
    return sum(args)

# 5. Keyword variable-length arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage examples
print(add(5, 3))                    # 8
print(greet())                      # Hello, Guest!
print(greet("Vivek"))               # Hello, Vivek!
print(person_info(age=22, name="Vivek", city="Dehradun"))
print(sum_all(1, 2, 3, 4, 5))       # 15
print_info(name="Vivek", age=22, city="Dehradun")
```

### Q4: What is the difference between `*args` and `**kwargs`?
**Answer:**
```python
# *args: Variable number of positional arguments (tuple)
def sum_numbers(*args):
    print(f"Args type: {type(args)}")  # <class 'tuple'>
    return sum(args)

# **kwargs: Variable number of keyword arguments (dict)
def print_details(**kwargs):
    print(f"Kwargs type: {type(kwargs)}")  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Usage
print(sum_numbers(1, 2, 3, 4))  # 10
print_details(name="Vivek", age=22, city="Dehradun")
```

---

## 📤 Return Values

### Q5: Can a function return multiple values?
**Answer:**
```python
# Yes! Python functions can return multiple values as a tuple
def get_name_age():
    return "Vivek", 22

def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Unpacking returned values
name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

min_val, max_val, avg_val = calculate_stats([1, 2, 3, 4, 5])
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")

# You can also return different data types
def get_person_info():
    return {
        "name": "Vivek",
        "age": 22,
        "skills": ["Python", "JavaScript"]
    }
```

### Q6: What happens if a function doesn't have a return statement?
**Answer:**
```python
def no_return():
    print("This function has no return statement")

def explicit_none():
    print("This function returns None explicitly")
    return None

# Both functions return None
result1 = no_return()      # None
result2 = explicit_none()  # None

print(result1 is None)  # True
print(result2 is None)  # True
```

---

## 🌍 Scope and Namespaces

### Q7: What is the difference between local and global scope?
**Answer:**
```python
# Global variable
global_var = "I'm global"

def test_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global var accessible: {global_var}")

# Outside function
print(f"Outside function: {global_var}")
# print(local_var)  # ❌ NameError: name 'local_var' is not defined

test_scope()
```

### Q8: How do you modify a global variable inside a function?
**Answer:**
```python
counter = 0

def increment_counter():
    global counter  # Declare that we want to modify global variable
    counter += 1
    return counter

def increment_without_global():
    # This creates a new local variable, doesn't modify global
    counter = 100
    return counter

print(f"Initial counter: {counter}")  # 0
print(f"After increment: {increment_counter()}")  # 1
print(f"Counter value: {counter}")  # 1
print(f"Local counter: {increment_without_global()}")  # 100
print(f"Global counter unchanged: {counter}")  # 1
```

---

## λ Lambda Functions

### Q9: When should you use lambda functions?
**Answer:**
```python
# Lambda functions are best for simple, one-line operations
# Especially useful with built-in functions like map, filter, sort

# 1. With map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 2. With filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# 3. With sorted()
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_grade)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# 4. Simple calculations
add = lambda x, y: x + y
print(add(5, 3))  # 8

# ❌ Don't use lambda for complex logic
# Use regular functions instead
```

---

## 🎨 Decorators

### Q10: What are decorators and how do they work?
**Answer:**
```python
# Decorator: A function that takes another function and extends its behavior

def timer_decorator(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

# Using decorator
@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

# This is equivalent to:
# slow_function = timer_decorator(slow_function)

result = slow_function()
print(result)
```

### Q11: How do you create a decorator with parameters?
**Answer:**
```python
def repeat(times):
    """Decorator that repeats a function n times"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Vivek")  # Prints "Hello, Vivek!" 3 times
```

---

## 🎯 Common Interview Questions

### Q12: What is recursion and when to use it?
**Answer:**
```python
# Recursion: Function calling itself
# Useful for problems that can be broken into smaller subproblems

def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative version (often more efficient)
def factorial_iterative(n):
    """Calculate factorial using iteration"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
```

### Q13: What is a closure?
**Answer:**
```python
# Closure: A function that remembers values from its enclosing scope

def outer_function(x):
    def inner_function(y):
        return x + y  # x is from outer scope
    return inner_function

# Create closure
add_five = outer_function(5)
add_ten = outer_function(10)

print(add_five(3))   # 8 (5 + 3)
print(add_ten(3))    # 13 (10 + 3)

# Practical example: Counter
def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

my_counter = create_counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3
```

### Q14: How do you handle function arguments efficiently?
**Answer:**
```python
# 1. Use default arguments for optional parameters
def create_user(name, age, email=None, phone=None):
    user = {"name": name, "age": age}
    if email:
        user["email"] = email
    if phone:
        user["phone"] = phone
    return user

# 2. Use *args for variable positional arguments
def calculate_average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# 3. Use **kwargs for variable keyword arguments
def build_profile(**kwargs):
    return kwargs

# 4. Use type hints for better code documentation
def greet_person(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

# Usage
user1 = create_user("Vivek", 22)
user2 = create_user("Alice", 25, email="alice@example.com")

avg = calculate_average(1, 2, 3, 4, 5)
profile = build_profile(name="Vivek", age=22, city="Dehradun")
```

---

## ⚡ Performance Tips

1. **Use `functools.lru_cache`** for expensive recursive functions
2. **Avoid global variables** when possible
3. **Use lambda functions sparingly** - prefer regular functions for complex logic
4. **Consider using `@staticmethod`** for utility functions
5. **Use type hints** for better code documentation and IDE support

---

## 🎓 Key Takeaways

- ✅ Functions are reusable blocks of code
- ✅ Use `*args` for variable positional arguments
- ✅ Use `**kwargs` for variable keyword arguments
- ✅ Functions can return multiple values
- ✅ Use `global` keyword to modify global variables
- ✅ Lambda functions are best for simple operations
- ✅ Decorators extend function behavior
- ✅ Closures remember values from outer scope

---

**Next: [Advanced Python Topics](./05_advanced_topics_interview.md)**
