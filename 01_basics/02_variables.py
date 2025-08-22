# ===============================
# 🐍 PYTHON VARIABLES – QUICK NOTES
# ===============================

# 1. What is a Variable?
# -------------------------------
# A variable is a name that stores data in memory.
# Python is dynamically typed → no need to declare type.

name = "Vivek"      # string
age = 22            # integer
pi = 3.14159        # float

print(name, age, pi)

# 2. Naming Rules
# -------------------------------
# ✅ Can contain letters, numbers, underscores (_)
# ✅ Must start with letter or underscore
# ❌ Cannot start with number
# ❌ Cannot use Python keywords

user_name = "Alice"
_user = "temp"
age2 = 30
# 2age = 25    # ❌ invalid
# for = "loop" # ❌ invalid

# 3. Types of Variables
# -------------------------------
integer_num = 10                # int
decimal_num = 10.5              # float
message = "Hello"               # str
is_active = True                # bool
numbers = [1, 2, 3]             # list
person = {"name": "Bob", "age": 25}  # dict

print(type(decimal_num))  # <class 'float'>

# 4. Reassignment
# -------------------------------
x = 5
print(x)
x = "Now I'm a string"
print(x)

# 5. Multiple Assignments
# -------------------------------
a, b, c = 1, 2, 3
x = y = z = 100
print(a, b, c, x, y, z)

# 6. Constants (by convention only)
# -------------------------------
PI = 3.14159
MAX_USERS = 100

# 7. Input into a Variable
# -------------------------------
# name_input = input("Enter your name: ")
# print("Hello,", name_input)

# ===============================
# END OF NOTES
# ===============================
