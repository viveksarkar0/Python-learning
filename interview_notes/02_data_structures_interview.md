# 🐍 Python Data Structures - Interview Questions & Answers

## 📋 Table of Contents
1. [Lists](#lists)
2. [Tuples](#tuples)
3. [Dictionaries](#dictionaries)
4. [Sets](#sets)
5. [Time Complexity](#time-complexity)
6. [Common Interview Questions](#common-interview-questions)

---

## 📝 Lists

### Q1: What are the main list operations and their time complexity?
**Answer:**
```python
# O(1) operations
my_list = [1, 2, 3, 4, 5]
my_list.append(6)        # Add to end
my_list.pop()           # Remove from end
my_list[0]              # Access by index
len(my_list)            # Get length

# O(n) operations
my_list.insert(0, 0)    # Insert at beginning
my_list.remove(3)       # Remove by value
my_list.index(4)        # Find index of value
3 in my_list            # Membership test

# O(n) operations
my_list.extend([7, 8])  # Extend with another list
my_list.reverse()       # Reverse in place
my_list.sort()          # Sort in place
```

### Q2: How do you remove duplicates from a list?
**Answer:**
```python
# Method 1: Using set (preserves order in Python 3.7+)
original = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(original))  # [1, 2, 3, 4, 5]

# Method 2: Using set (doesn't preserve order)
unique = list(set(original))

# Method 3: Manual loop (preserves order)
unique = []
for item in original:
    if item not in unique:
        unique.append(item)

# Method 4: List comprehension
unique = [x for i, x in enumerate(original) if x not in original[:i]]
```

### Q3: What is the difference between `append()` and `extend()`?
**Answer:**
```python
# append() adds the entire object
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

# extend() adds each element from the iterable
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5]

# extend() with string
list3 = [1, 2, 3]
list3.extend("abc")
print(list3)  # [1, 2, 3, 'a', 'b', 'c']
```

---

## 🔗 Tuples

### Q4: When should you use tuples instead of lists?
**Answer:**
```python
# Use tuples when:
# 1. Data is immutable
coordinates = (10, 20)
rgb_color = (255, 128, 0)

# 2. Data is used as dictionary keys
point_dict = {(1, 2): "point A", (3, 4): "point B"}

# 3. Data is returned from functions
def get_name_age():
    return ("Vivek", 22)

# 4. Performance is critical (tuples are faster)
import timeit
print(timeit.timeit('x=(1,2,3,4,5)', number=1000000))  # Faster
print(timeit.timeit('x=[1,2,3,4,5]', number=1000000))  # Slower
```

### Q5: How do you create a single-element tuple?
**Answer:**
```python
# Wrong way (creates int)
single = (5)        # This is just 5

# Correct way (comma is required)
single = (5,)       # This is a tuple
single = 5,         # Also works

print(type(single))  # <class 'tuple'>
```

---

## 📚 Dictionaries

### Q6: What are dictionary comprehensions?
**Answer:**
```python
# Basic dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
```

### Q7: How do you merge dictionaries?
**Answer:**
```python
# Python 3.5+ (unpacking)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Python 3.9+ (union operator)
merged = dict1 | dict2

# Using update()
dict1.update(dict2)

# Using dict() constructor
merged = dict(dict1, **dict2)
```

### Q8: What is the difference between `get()` and `[]`?
**Answer:**
```python
my_dict = {'a': 1, 'b': 2}

# Using [] (raises KeyError if key doesn't exist)
try:
    value = my_dict['c']
except KeyError:
    print("Key not found")

# Using get() (returns None or default value)
value = my_dict.get('c')           # None
value = my_dict.get('c', 0)        # 0 (default value)

# Safe way to increment
my_dict['count'] = my_dict.get('count', 0) + 1
```

---

## 🔄 Sets

### Q9: What are the main set operations?
**Answer:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union = set1 | set2  # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)

# Intersection
intersection = set1 & set2  # {3, 4}
intersection = set1.intersection(set2)

# Difference
diff = set1 - set2  # {1, 2}
diff = set1.difference(set2)

# Symmetric difference
sym_diff = set1 ^ set2  # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)
```

### Q10: How do you find the most common element in a list?
**Answer:**
```python
from collections import Counter

numbers = [1, 2, 2, 3, 2, 4, 5, 2, 6]

# Method 1: Using Counter
counter = Counter(numbers)
most_common = counter.most_common(1)[0][0]  # 2

# Method 2: Manual approach
def find_most_common(lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = count_dict.get(item, 0) + 1
    
    return max(count_dict, key=count_dict.get)

most_common = find_most_common(numbers)  # 2
```

---

## ⏱️ Time Complexity

### Common Operations Time Complexity:

| Operation | List | Tuple | Dict | Set |
|-----------|------|-------|------|-----|
| Access by index | O(1) | O(1) | N/A | N/A |
| Access by key | N/A | N/A | O(1) | N/A |
| Search | O(n) | O(n) | O(1) | O(1) |
| Insert at end | O(1) | N/A | O(1) | O(1) |
| Insert at beginning | O(n) | N/A | O(1) | O(1) |
| Delete | O(n) | N/A | O(1) | O(1) |

---

## 🎯 Common Interview Questions

### Q11: How do you check if two lists have the same elements?
**Answer:**
```python
def are_anagrams(list1, list2):
    return sorted(list1) == sorted(list2)

# Test
print(are_anagrams([1, 2, 3], [3, 1, 2]))  # True
print(are_anagrams([1, 2, 3], [1, 2, 4]))  # False
```

### Q12: How do you flatten a nested list?
**Answer:**
```python
# Method 1: List comprehension
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Method 2: Using itertools
from itertools import chain
flattened = list(chain.from_iterable(nested))

# Method 3: Recursive (for any depth)
def flatten_deep(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_deep(item))
        else:
            result.append(item)
    return result
```

---

## ⚡ Performance Tips

1. **Use sets for membership testing** (O(1) vs O(n))
2. **Use list comprehensions** instead of loops
3. **Use `collections.defaultdict`** for counting
4. **Use `collections.Counter`** for frequency analysis
5. **Use `enumerate()`** when you need both index and value

---

## 🎓 Key Takeaways

- ✅ Lists are mutable, tuples are immutable
- ✅ Dictionaries have O(1) average case for access
- ✅ Sets are perfect for unique elements and membership testing
- ✅ Choose the right data structure for your use case
- ✅ Consider time complexity for large datasets

---

**Next: [Control Flow Interview Questions](./03_control_flow_interview.md)**
