# ===============================
# 🐍 PYTHON DICTIONARIES – INTERVIEW NOTES
# ===============================

# ✅ What is a Dictionary?
# -------------------------------
# - Built-in data structure in Python.
# - Stores data in **key-value pairs**.
# - Features:
#     * Unordered (Python 3.7+: insertion order preserved)
#     * Mutable (can be modified)
#     * Keys must be immutable (str, int, tuple, etc.)
#     * Values can be any type

# Creating Dictionaries
student = {
    "name": "Vivek",
    "age": 21,
    "city": "Dehradun"
}

print("Dictionary:", student)

# ===============================
# 🔥 Accessing Elements
# ===============================

print("Name:", student["name"])         # direct access
print("City:", student.get("city"))     # safe access

# get() with default
print("Country:", student.get("country", "India"))

# ===============================
# 🔥 Adding & Updating Elements
# ===============================

student["age"] = 22        # update value
student["course"] = "BCA"  # add new key-value pair
print("After update:", student)

# ===============================
# 🔥 Removing Elements
# ===============================

student.pop("city")        # remove by key
print("After pop:", student)

removed = student.popitem()  # removes last inserted
print("After popitem:", student, "Removed:", removed)

del student["course"]      # delete by key
print("After del:", student)

student.clear()            # clear all items
print("After clear:", student)

# ===============================
# 🔥 Iterating a Dictionary
# ===============================

person = {"name": "Vivek", "age": 21, "city": "Dehradun"}

print("Keys:")
for key in person.keys():
    print(key)

print("Values:")
for value in person.values():
    print(value)

print("Items:")
for key, value in person.items():
    print(key, ":", value)

# ===============================
# 🔥 Dictionary Methods
# ===============================

data = {"a": 1, "b": 2, "c": 3}

print("Keys:", list(data.keys()))
print("Values:", list(data.values()))
print("Items:", list(data.items()))

print("Get with default:", data.get("d", "Not Found"))

data.update({"d": 4, "e": 5})   # add/update multiple
print("After update:", data)

copy_dict = data.copy()         # shallow copy
print("Copy:", copy_dict)

# ===============================
# 🔥 Dictionary Comprehension
# ===============================

squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)

even_squares = {x: x**2 for x in range(1, 10) if x % 2 == 0}
print("Even Squares:", even_squares)

# ===============================
# END OF INTERVIEW NOTES
# ===============================
