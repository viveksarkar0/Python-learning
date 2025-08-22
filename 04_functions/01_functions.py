# ===============================
# 🐍 PYTHON FUNCTIONS – INTERVIEW NOTES
# ===============================

# ✅ What is a Function?
# -------------------------------
# - A block of reusable code that performs a specific task.
# - Helps in modularity, readability, and reusability.
# - Defined using the `def` keyword.

# Basic Function
def greet():
    print("Hello, Python!")

greet()   # calling the function

# ===============================
# 🔥 Types of Functions
# ===============================

# 1. Function with Parameters
def add(a, b):
    return a + b

print("Sum:", add(5, 3))

# 2. Default Parameters
def welcome(name="Guest"):
    return f"Welcome, {name}!"

print(welcome())
print(welcome("Vivek"))

# 3. Keyword Arguments
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Vivek")

# 4. Variable-Length Arguments
def var_args(*args):   # *args → tuple
    print("Args:", args)

var_args(1, 2, 3, 4)

def var_kwargs(**kwargs):   # **kwargs → dict
    print("Kwargs:", kwargs)

var_kwargs(name="Vivek", age=21, city="Dehradun")

# 5. Return Multiple Values
def calc(a, b):
    return a+b, a-b, a*b

sum_, diff, prod = calc(10, 5)
print("Sum:", sum_, "Diff:", diff, "Prod:", prod)

# ===============================
# 📌 Advanced Functions
# ===============================

# Lambda (Anonymous) Functions
square = lambda x: x**2
print("Square of 4:", square(4))

# Map, Filter, Reduce
nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)

from functools import reduce
product = reduce(lambda x, y: x*y, nums)
print("Product:", product)

# ===============================
# 📌 Scope of Variables
# ===============================

x = 10   # global variable

def test_scope():
    x = 5   # local variable
    print("Inside function:", x)

test_scope()
print("Outside function:", x)

# Using global keyword
y = 20
def change_global():
    global y
    y = 50

change_global()
print("Changed global y:", y)

# ===============================
# 📌 Recursion
# ===============================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial 5:", factorial(5))

# ===============================
# END OF INTERVIEW NOTES
# ===============================
