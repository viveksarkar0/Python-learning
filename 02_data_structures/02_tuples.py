# ===============================
# 🐍 PYTHON TUPLES – INTERVIEW NOTES
# ===============================

# ✅ What is a Tuple?
# -------------------------------
# - A built-in data structure in Python.
# - Stores multiple items in one variable.
# - Features:
#     * Ordered (sequence is preserved)
#     * Immutable (cannot be changed after creation)
#     * Heterogeneous (can store different data types)
#     * Faster than lists (due to immutability)

fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4)
mixed = (1, "hello", 3.14, True)

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# ===============================
# 🔥 Interview-Style Questions
# ===============================

# 1. Difference between Tuple and List
# -------------------------------
my_tuple = (1, 2, 3)    # immutable
my_list = [1, 2, 3]     # mutable

print("Tuple:", my_tuple)
print("List:", my_list)

# my_tuple[0] = 99   # ❌ Error (immutable)
my_list[0] = 99       # ✅ Works
print("Modified List:", my_list)

# 2. Tuple with One Element
# -------------------------------
single = (5,)    # must include comma
not_tuple = (5)  # just an int
print("Single Tuple:", single, type(single))
print("Not a Tuple:", not_tuple, type(not_tuple))

# 3. Packing and Unpacking
# -------------------------------
person = ("Vivek", 21, "Dehradun")
name, age, city = person   # unpacking
print("Name:", name, "Age:", age, "City:", city)

# 4. Nested Tuples
# -------------------------------
nested = (1, (2, 3), (4, 5, (6, 7)))
print("Nested Tuple:", nested)
print("Access 5:", nested[2][1])
print("Access 7:", nested[2][2][1])

# 5. Tuple Methods
# -------------------------------
nums = (1, 2, 3, 2, 4, 2)

print("Count of 2:", nums.count(2))  # occurrences of element
print("Index of 3:", nums.index(3))  # first index of element

# 6. Converting between List and Tuple
# -------------------------------
my_list = [10, 20, 30]
my_tuple = tuple(my_list)   # list → tuple
print("List to Tuple:", my_tuple)

new_list = list(my_tuple)   # tuple → list
print("Tuple to List:", new_list)

# 7. Immutability Workaround
# -------------------------------
# Tuples are immutable, but you can convert to list and back
immutable = (1, 2, 3)
temp = list(immutable)
temp.append(4)
immutable = tuple(temp)
print("Modified Tuple:", immutable)

# ===============================
# 📌 Common Tuple Methods
# ===============================
# count(x) → returns number of occurrences of x
# index(x) → returns first index of x

# ===============================
# END OF INTERVIEW NOTES
# ===============================
