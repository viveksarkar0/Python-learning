# ===============================
# 🎯 BASIC PYTHON EXERCISES
# ===============================

# Exercise 1: Variables and Basic Operations
# -----------------------------------------
print("Exercise 1: Variables and Basic Operations")
print("-" * 40)

# TODO: Create variables for your name, age, and favorite number
# TODO: Print a sentence using these variables
# TODO: Calculate and print your age in months

# Your code here:
name = "Vivek"
age = 22
favorite_number = 7

print(f"My name is {name} and I am {age} years old.")
print(f"My favorite number is {favorite_number}.")
print(f"My age in months is {age * 12}.")

print("\n" + "="*50 + "\n")

# Exercise 2: String Operations
# -----------------------------
print("Exercise 2: String Operations")
print("-" * 40)

# TODO: Create a string with your full name
# TODO: Print the length of your name
# TODO: Print your name in uppercase and lowercase
# TODO: Print the first and last letter of your name

# Your code here:
full_name = "Vivek Sarkar"
print(f"My full name is: {full_name}")
print(f"Length of my name: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"First letter: {full_name[0]}")
print(f"Last letter: {full_name[-1]}")

print("\n" + "="*50 + "\n")

# Exercise 3: Lists and Basic Operations
# --------------------------------------
print("Exercise 3: Lists and Basic Operations")
print("-" * 40)

# TODO: Create a list of your favorite colors
# TODO: Add a new color to the list
# TODO: Remove the first color from the list
# TODO: Print the list and its length

# Your code here:
colors = ["blue", "green", "red", "purple"]
print(f"Original colors: {colors}")

colors.append("orange")
print(f"After adding orange: {colors}")

colors.pop(0)
print(f"After removing first color: {colors}")

print(f"Final list: {colors}")
print(f"Number of colors: {len(colors)}")

print("\n" + "="*50 + "\n")

# Exercise 4: Conditional Statements
# ----------------------------------
print("Exercise 4: Conditional Statements")
print("-" * 40)

# TODO: Create a variable with a number
# TODO: Check if the number is positive, negative, or zero
# TODO: Check if the number is even or odd

# Your code here:
number = 15

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print("\n" + "="*50 + "\n")

# Exercise 5: Loops
# -----------------
print("Exercise 5: Loops")
print("-" * 40)

# TODO: Print numbers from 1 to 10 using a for loop
# TODO: Print only even numbers from 1 to 20
# TODO: Calculate the sum of numbers from 1 to 100

# Your code here:
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("\nEven numbers 1 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

sum_1_to_100 = sum(range(1, 101))
print(f"\nSum of numbers 1 to 100: {sum_1_to_100}")

print("\n" + "="*50 + "\n")

# Exercise 6: Functions
# ---------------------
print("Exercise 6: Functions")
print("-" * 40)

# TODO: Create a function that calculates the area of a rectangle
# TODO: Create a function that checks if a number is prime
# TODO: Test both functions

# Your code here:
def rectangle_area(length, width):
    """Calculate area of rectangle"""
    return length * width

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test functions
print(f"Area of rectangle (5, 3): {rectangle_area(5, 3)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 25 prime? {is_prime(25)}")

print("\n" + "="*50 + "\n")

# Exercise 7: Dictionaries
# ------------------------
print("Exercise 7: Dictionaries")
print("-" * 40)

# TODO: Create a dictionary with your personal information
# TODO: Add a new key-value pair
# TODO: Print all keys and values

# Your code here:
personal_info = {
    "name": "Vivek",
    "age": 22,
    "city": "Dehradun",
    "occupation": "Student"
}

personal_info["hobby"] = "Programming"

print("Personal Information:")
for key, value in personal_info.items():
    print(f"{key.capitalize()}: {value}")

print("\n" + "="*50 + "\n")

# Exercise 8: Error Handling
# --------------------------
print("Exercise 8: Error Handling")
print("-" * 40)

# TODO: Create a function that safely divides two numbers
# TODO: Test with valid and invalid inputs

# Your code here:
def safe_divide(a, b):
    """Safely divide a by b"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide valid numbers!"

# Test the function
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'abc' = {safe_divide(10, 'abc')}")

print("\n" + "="*50 + "\n")

print("🎉 All exercises completed!")
print("💡 Try modifying the values and see what happens!")
