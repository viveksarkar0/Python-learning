# ===============================
# 🎯 ADVANCED PYTHON EXERCISES
# ===============================

# ===============================
# 🏗️ OBJECT-ORIENTED PROGRAMMING EXERCISES
# ===============================

print("Exercise 1: Create a Bank Account Class")
print("-" * 50)

# TODO: Create a BankAccount class with the following features:
# - Account number, holder name, balance
# - Methods: deposit, withdraw, get_balance
# - Validation for insufficient funds
# - Transaction history

class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transactions

# Test the BankAccount class
account = BankAccount("12345", "Vivek", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Should fail
print(f"Balance: ${account.get_balance()}")
print("Transaction history:", account.get_transaction_history())

print("\n" + "="*60 + "\n")

# ===============================
# 📁 FILE HANDLING EXERCISES
# ===============================

print("Exercise 2: File Processing")
print("-" * 50)

# TODO: Create a function that:
# - Reads a text file
# - Counts words, lines, and characters
# - Finds the most common word
# - Saves statistics to a new file

def analyze_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            
            # Count statistics
            line_count = len(lines)
            word_count = len(words)
            char_count = len(content)
            
            # Find most common word
            word_freq = {}
            for word in words:
                word = word.lower().strip('.,!?;:')
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
            
            most_common_word = max(word_freq, key=word_freq.get) if word_freq else "None"
            
            # Save statistics
            stats = f"""Text File Analysis
==================
File: {filename}
Lines: {line_count}
Words: {word_count}
Characters: {char_count}
Most common word: '{most_common_word}' (appears {word_freq.get(most_common_word, 0)} times)
"""
            
            with open('analysis_results.txt', 'w') as output_file:
                output_file.write(stats)
            
            print(stats)
            print("Results saved to 'analysis_results.txt'")
            
    except FileNotFoundError:
        print(f"File '{filename}' not found!")

# Create a sample file for testing
sample_text = """Python is a programming language.
Python is easy to learn and powerful.
Python has many libraries and frameworks.
Python is used for web development, data science, and more.
Python is awesome!"""

with open('sample_text.txt', 'w') as file:
    file.write(sample_text)

# Analyze the file
analyze_text_file('sample_text.txt')

print("\n" + "="*60 + "\n")

# ===============================
# 🔍 DATA PROCESSING EXERCISES
# ===============================

print("Exercise 3: Data Processing")
print("-" * 50)

# TODO: Process a list of student records and:
# - Calculate average score
# - Find highest and lowest scores
# - Group by grade level
# - Create a summary report

students_data = [
    {"name": "Alice", "age": 20, "score": 85, "grade": "A"},
    {"name": "Bob", "age": 19, "score": 92, "grade": "A"},
    {"name": "Charlie", "age": 21, "score": 78, "grade": "B"},
    {"name": "Diana", "age": 20, "score": 95, "grade": "A"},
    {"name": "Eve", "age": 22, "score": 88, "grade": "B"},
    {"name": "Frank", "age": 19, "score": 76, "grade": "C"},
    {"name": "Grace", "age": 21, "score": 91, "grade": "A"},
    {"name": "Henry", "age": 20, "score": 82, "grade": "B"}
]

def analyze_student_data(students):
    if not students:
        return "No student data provided"
    
    # Calculate statistics
    scores = [student["score"] for student in students]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    # Group by grade
    grade_groups = {}
    for student in students:
        grade = student["grade"]
        if grade not in grade_groups:
            grade_groups[grade] = []
        grade_groups[grade].append(student)
    
    # Create report
    report = f"""STUDENT DATA ANALYSIS
====================
Total Students: {len(students)}
Average Score: {avg_score:.2f}
Highest Score: {max_score}
Lowest Score: {min_score}

Grade Distribution:
"""
    
    for grade in sorted(grade_groups.keys()):
        students_in_grade = grade_groups[grade]
        avg_grade_score = sum(s["score"] for s in students_in_grade) / len(students_in_grade)
        report += f"Grade {grade}: {len(students_in_grade)} students (avg: {avg_grade_score:.2f})\n"
    
    # Top performers
    top_students = sorted(students, key=lambda x: x["score"], reverse=True)[:3]
    report += "\nTop 3 Students:\n"
    for i, student in enumerate(top_students, 1):
        report += f"{i}. {student['name']} - Score: {student['score']}, Grade: {student['grade']}\n"
    
    return report

print(analyze_student_data(students_data))

print("\n" + "="*60 + "\n")

# ===============================
# 🔄 ALGORITHM EXERCISES
# ===============================

print("Exercise 4: Algorithm Implementation")
print("-" * 50)

# TODO: Implement the following algorithms:
# 1. Binary Search
# 2. Bubble Sort
# 3. Find duplicates in a list
# 4. Check if two strings are anagrams

def binary_search(arr, target):
    """Binary search implementation"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_duplicates(arr):
    """Find duplicate elements in a list"""
    seen = set()
    duplicates = set()
    
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Count characters
    char_count = {}
    
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0

# Test the algorithms
print("Testing Binary Search:")
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(numbers, target)
print(f"Found {target} at index: {result}")

print("\nTesting Bubble Sort:")
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(unsorted.copy())
print(f"Original: {unsorted}")
print(f"Sorted: {sorted_arr}")

print("\nTesting Duplicate Finder:")
duplicate_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
duplicates = find_duplicates(duplicate_list)
print(f"List: {duplicate_list}")
print(f"Duplicates: {duplicates}")

print("\nTesting Anagram Checker:")
test_cases = [
    ("listen", "silent"),
    ("hello", "world"),
    ("debit card", "bad credit"),
    ("python", "typhon")
]

for str1, str2 in test_cases:
    result = are_anagrams(str1, str2)
    print(f"'{str1}' and '{str2}': {result}")

print("\n" + "="*60 + "\n")

# ===============================
# 🎯 ADVANCED FUNCTION EXERCISES
# ===============================

print("Exercise 5: Advanced Functions")
print("-" * 50)

# TODO: Create advanced functions:
# 1. Decorator that measures execution time
# 2. Generator function for Fibonacci numbers
# 3. Function with multiple return types
# 4. Recursive function for factorial

import time
from typing import Union, List, Dict

def timer_decorator(func):
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def fibonacci_generator(n: int):
    """Generator function for Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def process_data(data: Union[str, List, Dict]) -> Dict:
    """Function that processes different data types"""
    if isinstance(data, str):
        return {"type": "string", "length": len(data), "uppercase": data.upper()}
    elif isinstance(data, list):
        return {"type": "list", "length": len(data), "sum": sum(data) if all(isinstance(x, (int, float)) for x in data) else None}
    elif isinstance(data, dict):
        return {"type": "dict", "keys": list(data.keys()), "values": list(data.values())}
    else:
        return {"type": "unknown", "data": str(data)}

def factorial_recursive(n: int) -> int:
    """Recursive factorial function"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test the advanced functions
@timer_decorator
def slow_function():
    """A function that takes some time to execute"""
    time.sleep(0.1)
    return "Done!"

print("Testing Timer Decorator:")
result = slow_function()

print("\nTesting Fibonacci Generator:")
fib_gen = fibonacci_generator(10)
fib_numbers = list(fib_gen)
print(f"First 10 Fibonacci numbers: {fib_numbers}")

print("\nTesting Multi-type Function:")
test_data = [
    "Hello World",
    [1, 2, 3, 4, 5],
    {"name": "Vivek", "age": 22},
    42
]

for data in test_data:
    result = process_data(data)
    print(f"Input: {data}")
    print(f"Output: {result}")

print("\nTesting Recursive Factorial:")
try:
    for n in range(6):
        result = factorial_recursive(n)
        print(f"Factorial of {n}: {result}")
except ValueError as e:
    print(f"Error: {e}")

print("\n" + "="*60 + "\n")

# ===============================
# 🎮 MINI-PROJECT: SIMPLE GAME
# ===============================

print("Exercise 6: Number Guessing Game")
print("-" * 50)

import random

class NumberGuessingGame:
    """A simple number guessing game"""
    
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
    
    def play(self):
        """Main game loop"""
        print("🎮 Welcome to the Number Guessing Game!")
        print(f"I'm thinking of a number between 1 and 100.")
        print(f"You have {self.max_attempts} attempts to guess it.")
        
        while self.attempts < self.max_attempts:
            try:
                guess = int(input(f"\nAttempt {self.attempts + 1}: Enter your guess (1-100): "))
                
                if guess < 1 or guess > 100:
                    print("❌ Please enter a number between 1 and 100!")
                    continue
                
                self.attempts += 1
                
                if guess == self.secret_number:
                    print(f"🎉 Congratulations! You guessed it in {self.attempts} attempts!")
                    return True
                elif guess < self.secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("📉 Too high! Try a lower number.")
                
                remaining = self.max_attempts - self.attempts
                print(f"Attempts remaining: {remaining}")
                
            except ValueError:
                print("❌ Please enter a valid number!")
        
        print(f"😔 Game Over! The number was {self.secret_number}")
        return False

# Play the game
game = NumberGuessingGame()
# Uncomment the next line to play the game
# game.play()

print("Game class created! Uncomment the game.play() line to play.")

print("\n" + "="*60 + "\n")

print("🎉 All advanced exercises completed!")
print("💡 These exercises cover:")
print("   - Object-Oriented Programming")
print("   - File Handling")
print("   - Data Processing")
print("   - Algorithm Implementation")
print("   - Advanced Functions")
print("   - Mini-Project Development")
print("\n🚀 Keep practicing and building more complex applications!")
