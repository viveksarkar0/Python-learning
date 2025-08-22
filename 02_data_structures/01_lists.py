# ===============================
# 🐍 PYTHON LISTS – INTERVIEW NOTES
# ===============================

# ✅ What is a List?
# -------------------------------
# - A built-in data structure in Python.
# - Stores multiple items in one variable.
# - Features:
#     * Ordered (sequence is preserved)
#     * Mutable (can be modified)
#     * Heterogeneous (can store different data types)
#     * Dynamic (size can change)

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "hello", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

# ===============================
# 🔥 Interview-Style Questions
# ===============================

# 1. Difference between List and Tuple
# -------------------------------
my_list = [1, 2, 3]      # mutable
my_tuple = (1, 2, 3)     # immutable

print("List before:", my_list)
my_list[0] = 99
print("List after:", my_list)
# my_tuple[0] = 99   # ❌ would cause error (immutable)

# 2. Adding and Removing Elements
# -------------------------------
fruits.append("orange")      # add at end
fruits.insert(1, "kiwi")     # insert at position
print("After adding:", fruits)

fruits.remove("banana")      # remove by value
popped = fruits.pop()        # remove last element
print("After removing:", fruits, "Popped:", popped)

# 3. Copying a List
# -------------------------------
a = [1, 2, 3]
b = a.copy()     # safe copy
c = a[:]         # slicing copy
a[0] = 100
print("Original:", a, "Copy b:", b, "Copy c:", c)

# 4. Iterating with Index
# -------------------------------
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print("Index:", i, "Value:", val)

# 5. List Comprehension
# -------------------------------
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

even_nums = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", even_nums)

# 6. Nested Lists
# -------------------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix row 0:", matrix[0])
print("Matrix[1][2]:", matrix[1][2])  # → 6

# ===============================
# 📌 Common List Methods
# ===============================

nums = [5, 2, 9, 1, 5, 6]

print("Original:", nums)

nums.extend([7, 8])    # extend with another list
print("Extend:", nums)

nums.sort()            # sort ascending
print("Sorted:", nums)

nums.sort(reverse=True)  # sort descending
print("Sorted Desc:", nums)

nums.reverse()         # reverse list
print("Reversed:", nums)

print("Count of 5:", nums.count(5))   # count occurrences
print("Index of 9:", nums.index(9))   # first index of element

nums.clear()           # remove all elements
print("Cleared:", nums)

# ===============================
# END OF INTERVIEW NOTES
# ===============================
