# ===============================
# 🐍 PYTHON CONDITIONALS – INTERVIEW NOTES
# ===============================

# ✅ What are Conditionals?
# -------------------------------
# - Used to make decisions in a program.
# - Executes code blocks based on conditions (True/False).
# - Keywords: if, elif, else

# ===============================
# 🔥 Basic if-else
# ===============================

x = 10

if x > 0:
    print("Positive number")
else:
    print("Non-positive number")

# ===============================
# 🔥 if-elif-else ladder
# ===============================

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# ===============================
# 🔥 Nested if
# ===============================

num = 12

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative or Zero")

# ===============================
# 🔥 Ternary / One-Line if-else
# ===============================

age = 18
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# ===============================
# 🔥 Logical Operators
# ===============================
a, b = 5, 15

if a > 0 and b > 10:
    print("Both conditions are True")

if a < 0 or b > 10:
    print("At least one condition is True")

if not (a > 10):
    print("a is NOT greater than 10")

# ===============================
# 🔥 Membership Operators
# ===============================

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "mango" not in fruits:
    print("Mango is NOT in the list")

# ===============================
# 🔥 Identity Operators
# ===============================

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True → same object
print(x is z)      # False → different objects
print(x == z)      # True → values are equal

# ===============================
# END OF INTERVIEW NOTES
# ===============================
