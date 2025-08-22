# ===============================
# 🐍 PYTHON NUMBERS – QUICK NOTES
# ===============================

# 1. Types of Numbers in Python
# -------------------------------
integer_num = 10        # int (whole number)
float_num = 10.5        # float (decimal)
complex_num = 2 + 3j    # complex (real + imaginary)

print(type(integer_num))   # <class 'int'>
print(type(float_num))     # <class 'float'>
print(type(complex_num))   # <class 'complex'>

# 2. Basic Arithmetic Operators
# -------------------------------
a, b = 15, 4

print(a + b)   # Addition → 19
print(a - b)   # Subtraction → 11
print(a * b)   # Multiplication → 60
print(a / b)   # Division (float) → 3.75
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus (remainder) → 3
print(a ** b)  # Exponentiation → 15^4 = 50625

# 3. Operator Precedence (BODMAS)
# -------------------------------
result = 2 + 3 * 4    # 2 + (3*4) = 14
print(result)
result = (2 + 3) * 4  # (2+3)*4 = 20
print(result)

# 4. Type Conversion
# -------------------------------
x = 10
y = 3.5
z = "100"

print(float(x))     # int → float → 10.0
print(int(y))       # float → int → 3
print(int(z))       # string → int → 100
print(str(x))       # int → str → "10"

# 5. Math Functions (import math module)
# -------------------------------
import math

print(abs(-7))        # Absolute value → 7
print(pow(2, 3))      # 2^3 = 8 (same as 2**3)
print(round(3.7))     # Round to nearest int → 4
print(math.floor(3.7))# Floor → 3
print(math.ceil(3.7)) # Ceil → 4
print(math.sqrt(16))  # Square root → 4.0
print(math.factorial(5))  # 5! = 120

# 6. Random Numbers (import random module)
# -------------------------------
import random

print(random.randint(1, 10))   # Random int between 1 and 10
print(random.random())         # Random float (0.0 to 1.0)
print(random.uniform(1, 5))    # Random float (1.0 to 5.0)
print(random.choice([10, 20, 30, 40]))  # Random pick from list

# 7. Augmented Assignment
# -------------------------------
num = 10
num += 5   # num = num + 5
print(num) # 15
num *= 2   # num = num * 2
print(num) # 30

# 8. Complex Numbers
# -------------------------------
c1 = 2 + 3j
c2 = 1 + 4j

print(c1 + c2)   # (2+3j) + (1+4j) = (3+7j)
print(c1.real)   # real part → 2.0
print(c1.imag)   # imaginary part → 3.0

# ===============================
# END OF NOTES
# ===============================
