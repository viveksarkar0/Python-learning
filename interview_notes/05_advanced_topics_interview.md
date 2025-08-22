# 🐍 Advanced Python Topics - Interview Questions & Answers

## 📋 Table of Contents
1. [Object-Oriented Programming](#object-oriented-programming)
2. [File Handling](#file-handling)
3. [Exception Handling](#exception-handling)
4. [Modules and Packages](#modules-and-packages)
5. [Generators and Iterators](#generators-and-iterators)
6. [Context Managers](#context-managers)
7. [Common Interview Questions](#common-interview-questions)

---

## 🏗️ Object-Oriented Programming

### Q1: What are the four pillars of OOP?
**Answer:**
```python
# 1. ENCAPSULATION - Bundling data and methods that operate on that data
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

# 2. INHERITANCE - Creating new classes from existing ones
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# 3. POLYMORPHISM - Same interface, different implementations
def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
print(animal_sound(dog))  # "Woof!"

# 4. ABSTRACTION - Hiding complex implementation details
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.width * self.height
```

### Q2: What is the difference between `__init__` and `__new__`?
**Answer:**
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        """Called before __init__, returns the instance"""
        print("__new__ called")
        return super().__new__(cls)
    
    def __init__(self, value):
        """Called after __new__, initializes the instance"""
        print("__init__ called")
        self.value = value

# __new__ is called first, then __init__
obj = MyClass(42)
```

**🔥 Interview Tip:** `__new__` is a static method that creates the instance, while `__init__` initializes it.

### Q3: What are class methods and static methods?
**Answer:**
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Class method - receives class as first argument"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_valid_date(date_string):
        """Static method - no access to class or instance"""
        try:
            year, month, day = map(int, date_string.split('-'))
            return 1 <= month <= 12 and 1 <= day <= 31
        except:
            return False

# Using class method
date = Date.from_string("2023-12-25")

# Using static method
is_valid = Date.is_valid_date("2023-12-25")
```

---

## 📁 File Handling

### Q4: What is the difference between `'r'`, `'w'`, `'a'`, and `'r+'` modes?
**Answer:**
```python
# 'r' - Read mode (default)
with open('file.txt', 'r') as f:
    content = f.read()

# 'w' - Write mode (overwrites existing content)
with open('file.txt', 'w') as f:
    f.write("New content")

# 'a' - Append mode (adds to existing content)
with open('file.txt', 'a') as f:
    f.write("\nAdditional content")

# 'r+' - Read and write mode
with open('file.txt', 'r+') as f:
    content = f.read()
    f.write("More content")

# 'w+' - Write and read mode (truncates file)
with open('file.txt', 'w+') as f:
    f.write("Content")
    f.seek(0)  # Go to beginning
    content = f.read()
```

### Q5: How do you handle different file encodings?
**Answer:**
```python
# UTF-8 (default)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# ASCII
with open('file.txt', 'r', encoding='ascii') as f:
    content = f.read()

# Latin-1
with open('file.txt', 'r', encoding='latin-1') as f:
    content = f.read()

# Handle encoding errors
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    # Try different encoding
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

---

## ⚠️ Exception Handling

### Q6: What is the difference between `try-except` and `try-finally`?
**Answer:**
```python
# try-except: Handle specific exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# try-finally: Always execute cleanup code
try:
    file = open('data.txt', 'r')
    content = file.read()
finally:
    file.close()  # Always executed

# try-except-finally: Handle exceptions and cleanup
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup code always runs")

# try-except-else: Execute code when no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")  # Only runs if no exception
```

### Q7: How do you create custom exceptions?
**Answer:**
```python
class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

class AgeError(ValidationError):
    """Specific exception for age validation"""
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise AgeError(age, "Age cannot be negative")
    elif age > 150:
        raise AgeError(age, "Age seems unrealistic")
    return True

# Using custom exceptions
try:
    validate_age(-5)
except AgeError as e:
    print(f"Age error: {e.message}, Age: {e.age}")
except ValidationError as e:
    print(f"Validation error: {e}")
```

---

## 📦 Modules and Packages

### Q8: What is the difference between a module and a package?
**Answer:**
```python
# MODULE: A single Python file
# math.py
import math
print(math.pi)

# PACKAGE: A directory containing multiple modules
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

# Using a package
from mypackage import module1, module2
from mypackage.module1 import some_function

# __init__.py makes a directory a package
# It can be empty or contain initialization code
```

### Q9: How do you handle circular imports?
**Answer:**
```python
# Problem: Circular import
# file1.py
from file2 import function_b

def function_a():
    return function_b()

# file2.py
from file1 import function_a

def function_b():
    return function_a()

# Solution 1: Import inside function
def function_a():
    from file2 import function_b
    return function_b()

# Solution 2: Restructure code
# Move common functionality to a third module

# Solution 3: Use dependency injection
class ServiceA:
    def __init__(self, service_b):
        self.service_b = service_b
    
    def do_something(self):
        return self.service_b.help()
```

---

## 🔄 Generators and Iterators

### Q10: What is the difference between generators and iterators?
**Answer:**
```python
# ITERATOR: Object with __iter__ and __next__ methods
class NumberIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

# GENERATOR: Function using yield
def number_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

# Using iterator
iterator = NumberIterator(1, 5)
for num in iterator:
    print(num)

# Using generator
generator = number_generator(1, 5)
for num in generator:
    print(num)

# Generator expression
squares = (x**2 for x in range(5))
```

### Q11: When should you use generators?
**Answer:**
```python
# Use generators for:
# 1. Large datasets (memory efficient)
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# 2. Infinite sequences
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 3. Processing pipelines
def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

# Pipeline
numbers = range(10)
even_squares = square_numbers(filter_even(numbers))
```

---

## 🎯 Context Managers

### Q12: What are context managers and how do you create them?
**Answer:**
```python
# Context manager using class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using context manager
with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')

# Context manager using decorator
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")

# Using timer context manager
with timer():
    # Some time-consuming operation
    import time
    time.sleep(1)
```

---

## 🎯 Common Interview Questions

### Q13: How do you implement a singleton pattern?
**Answer:**
```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = []

# Using singleton
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True

# Alternative using decorator
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "Connected"
```

### Q14: How do you implement a factory pattern?
**Answer:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat
        }
        return animals.get(animal_type.lower())()

# Using factory
factory = AnimalFactory()
dog = factory.create_animal('dog')
cat = factory.create_animal('cat')

print(dog.make_sound())  # "Woof!"
print(cat.make_sound())  # "Meow!"
```

### Q15: How do you handle memory management in Python?
**Answer:**
```python
import gc
import sys

# 1. Garbage collection
gc.collect()  # Force garbage collection

# 2. Memory profiling
import tracemalloc
tracemalloc.start()

# Your code here
data = [i for i in range(1000000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")

# 3. Using weak references
import weakref

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def get(self, key):
        return self._cache.get(key)
    
    def set(self, key, value):
        self._cache[key] = value

# 4. Context managers for resource management
class ResourceManager:
    def __enter__(self):
        # Acquire resource
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Release resource
        pass
```

---

## ⚡ Performance Tips

1. **Use `__slots__`** for memory optimization in classes
2. **Use `collections.defaultdict`** instead of regular dict with default values
3. **Use `itertools`** for efficient iteration
4. **Use `functools.lru_cache`** for memoization
5. **Use `__enter__` and `__exit__`** for resource management

---

## 🎓 Key Takeaways

- ✅ OOP provides structure and reusability
- ✅ Use context managers for resource management
- ✅ Generators are memory-efficient for large datasets
- ✅ Custom exceptions improve error handling
- ✅ Design patterns solve common problems
- ✅ Memory management is automatic but can be optimized

---

**🎉 Congratulations! You've completed the comprehensive Python learning journey!**
