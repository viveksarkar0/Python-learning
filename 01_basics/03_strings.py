# ===============================
# 🐍 PYTHON STRINGS – QUICK NOTES
# ===============================

# 1. Creating Strings
# -------------------------------
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line string"""

print(single_quote, double_quote)
print(multi_line)

# 2. String Concatenation (Joining)
# -------------------------------
first = "Vivek"
last = "Sarkar"
full_name = first + " " + last
print("Full Name:", full_name)

# 3. String Repetition
# -------------------------------
laugh = "ha" * 3
print(laugh)   # "hahaha"

# 4. Indexing and Slicing
# -------------------------------
word = "Python"
print(word[0])      # P  (first character)
print(word[-1])     # n  (last character)
print(word[0:4])    # Pyth (slice from index 0 to 3)
print(word[:3])     # Pyt
print(word[2:])     # thon

# 5. Useful String Methods
# -------------------------------
msg = "  hello world  "

print(msg.upper())      # HELLO WORLD
print(msg.lower())      # hello world
print(msg.title())      # Hello World
print(msg.strip())      # removes spaces → "hello world"
print(msg.replace("world", "Python"))  # hello Python
print(msg.split())      # ['hello', 'world']
print("-".join(["a", "b", "c"]))       # a-b-c

# 6. String Searching
# -------------------------------
text = "I love Python programming"
print("love" in text)       # True
print("Java" not in text)   # True
print(text.find("Python"))  # index of substring → 7
print(text.find("Java"))    # -1 if not found

# 7. String Formatting
# -------------------------------
name = "Vivek"
age = 22

# Old style
print("My name is %s and I am %d years old." % (name, age))

# str.format()
print("My name is {} and I am {} years old.".format(name, age))
print("My name is {0} and I am {1} years old.".format(name, age))

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# 8. Escaping Characters
# -------------------------------
quote = "He said, \"Python is awesome!\""
path = "C:\\Users\\Vivek\\Desktop"
print(quote)
print(path)

# 9. Raw Strings (ignore escape sequences)
# -------------------------------
raw_path = r"C:\Users\Vivek\Desktop"
print(raw_path)

# 10. Multiline String Tricks
# -------------------------------
multiline_text = """Line1
Line2
Line3"""
print(multiline_text)

# ===============================
# END OF NOTES
# ===============================
