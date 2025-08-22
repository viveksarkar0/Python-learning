# ===============================
# 🐍 PYTHON INPUT() – QUICK NOTES
# ===============================

# 1. Basic Input
# -------------------------------
# input() always returns a string
name = input("Enter your name: ")
print("Hello,", name)

# 2. Input with Numbers (Type Casting)
# -------------------------------
# By default input() → string, so convert with int() or float()
age = int(input("Enter your age: "))
print("Next year you will be:", age + 1)

height = float(input("Enter your height in meters: "))
print("Height in cm:", height * 100)

# 3. Multiple Inputs in One Line
# -------------------------------
# split() → breaks input into a list of strings
a, b = input("Enter two numbers separated by space: ").split()
print("a =", a, "b =", b)

# Convert them to integers
a, b = map(int, input("Enter two numbers again: ").split())
print("Sum =", a + b)

# 4. Taking List Input
# -------------------------------
# Example: user enters → 10 20 30 40
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Numbers List:", nums)

# 5. Input with Prompt Formatting
# -------------------------------
username = input("👤 Username: ")
password = input("🔑 Password: ")
print(f"Welcome {username}, your password length is {len(password)} characters")

# 6. Handling Input Safely
# -------------------------------
# Use try-except for numeric input
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("❌ That was not a valid integer!")

# ===============================
# END OF NOTES
# ===============================
