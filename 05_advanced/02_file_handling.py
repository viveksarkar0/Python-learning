# ===============================
# 📁 PYTHON FILE HANDLING
# ===============================

# ===============================
# 📖 READING FILES
# ===============================

def read_file_basic():
    """Basic file reading operations"""
    
    # Method 1: Reading entire file at once
    print("=== Reading entire file ===")
    try:
        with open('sample.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found. Creating sample file...")
        create_sample_file()
        with open('sample.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

def read_file_line_by_line():
    """Reading file line by line"""
    
    print("\n=== Reading line by line ===")
    try:
        with open('sample.txt', 'r') as file:
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")

def read_file_into_list():
    """Reading file into a list of lines"""
    
    print("\n=== Reading into list ===")
    try:
        with open('sample.txt', 'r') as file:
            lines = file.readlines()
            print(f"Total lines: {len(lines)}")
            for i, line in enumerate(lines):
                print(f"Line {i+1}: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")

def read_file_with_encoding():
    """Reading file with specific encoding"""
    
    print("\n=== Reading with encoding ===")
    try:
        # UTF-8 is the default encoding
        with open('sample.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print("Content with UTF-8 encoding:")
            print(content)
    except FileNotFoundError:
        print("File not found!")

# ===============================
# ✍️ WRITING FILES
# ===============================

def write_file_basic():
    """Basic file writing operations"""
    
    print("\n=== Writing to file ===")
    
    # Method 1: Write entire content at once
    content = """Hello, this is a sample file.
This is the second line.
This is the third line.
Python file handling is awesome!"""
    
    with open('output.txt', 'w') as file:
        file.write(content)
    
    print("File 'output.txt' created successfully!")
    
    # Read back to verify
    with open('output.txt', 'r') as file:
        print("Content written:")
        print(file.read())

def write_file_line_by_line():
    """Writing file line by line"""
    
    print("\n=== Writing line by line ===")
    
    lines = [
        "First line of the file",
        "Second line with some data",
        "Third line with numbers: 1, 2, 3",
        "Fourth line with special characters: @#$%",
        "Fifth and final line"
    ]
    
    with open('lines.txt', 'w') as file:
        for line in lines:
            file.write(line + '\n')
    
    print("File 'lines.txt' created with multiple lines!")
    
    # Read back to verify
    with open('lines.txt', 'r') as file:
        print("Content written:")
        for line in file:
            print(f"  {line.strip()}")

def append_to_file():
    """Appending content to existing file"""
    
    print("\n=== Appending to file ===")
    
    # First, create a file
    with open('append_demo.txt', 'w') as file:
        file.write("Original content\n")
    
    print("Original file created.")
    
    # Append new content
    with open('append_demo.txt', 'a') as file:
        file.write("This line was appended\n")
        file.write("Another appended line\n")
        file.write("Final appended line\n")
    
    print("Content appended successfully!")
    
    # Read back to verify
    with open('append_demo.txt', 'r') as file:
        print("Final content:")
        print(file.read())

# ===============================
# 📊 CSV FILE HANDLING
# ===============================

import csv

def create_csv_file():
    """Creating and writing to CSV file"""
    
    print("\n=== CSV File Operations ===")
    
    # Sample data
    students = [
        ['Name', 'Age', 'Grade', 'City'],
        ['Vivek', 22, 'A', 'Dehradun'],
        ['Alice', 20, 'B', 'Mumbai'],
        ['Bob', 21, 'A', 'Delhi'],
        ['Charlie', 19, 'C', 'Bangalore']
    ]
    
    # Write to CSV
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)
    
    print("CSV file 'students.csv' created successfully!")

def read_csv_file():
    """Reading from CSV file"""
    
    print("\n=== Reading CSV ===")
    
    try:
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"  {row}")
    except FileNotFoundError:
        print("CSV file not found!")

def read_csv_as_dict():
    """Reading CSV as dictionary"""
    
    print("\n=== Reading CSV as Dictionary ===")
    
    try:
        with open('students.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"  {row['Name']} is {row['Age']} years old, Grade: {row['Grade']}")
    except FileNotFoundError:
        print("CSV file not found!")

# ===============================
# 📄 JSON FILE HANDLING
# ===============================

import json

def create_json_file():
    """Creating and writing to JSON file"""
    
    print("\n=== JSON File Operations ===")
    
    # Sample data
    data = {
        "students": [
            {
                "name": "Vivek",
                "age": 22,
                "grade": "A",
                "city": "Dehradun",
                "skills": ["Python", "JavaScript", "SQL"]
            },
            {
                "name": "Alice",
                "age": 20,
                "grade": "B",
                "city": "Mumbai",
                "skills": ["Java", "Python", "HTML"]
            },
            {
                "name": "Bob",
                "age": 21,
                "grade": "A",
                "city": "Delhi",
                "skills": ["C++", "Python", "CSS"]
            }
        ],
        "total_students": 3,
        "average_age": 21.0
    }
    
    # Write to JSON file
    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    print("JSON file 'students.json' created successfully!")

def read_json_file():
    """Reading from JSON file"""
    
    print("\n=== Reading JSON ===")
    
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
            
        print("JSON data loaded:")
        print(f"Total students: {data['total_students']}")
        print(f"Average age: {data['average_age']}")
        
        print("\nStudent details:")
        for student in data['students']:
            print(f"  {student['name']} - Age: {student['age']}, Grade: {student['grade']}")
            print(f"    Skills: {', '.join(student['skills'])}")
            
    except FileNotFoundError:
        print("JSON file not found!")

# ===============================
# 🔍 FILE OPERATIONS
# ===============================

import os
import shutil

def file_operations():
    """Various file operations"""
    
    print("\n=== File Operations ===")
    
    # Check if file exists
    filename = 'sample.txt'
    if os.path.exists(filename):
        print(f"File '{filename}' exists")
        
        # Get file information
        file_size = os.path.getsize(filename)
        print(f"File size: {file_size} bytes")
        
        # Get file modification time
        mod_time = os.path.getmtime(filename)
        print(f"Last modified: {mod_time}")
        
        # Copy file
        shutil.copy(filename, 'sample_backup.txt')
        print("File copied to 'sample_backup.txt'")
        
        # Rename file
        os.rename('sample_backup.txt', 'sample_renamed.txt')
        print("File renamed to 'sample_renamed.txt'")
        
    else:
        print(f"File '{filename}' does not exist")

def directory_operations():
    """Directory operations"""
    
    print("\n=== Directory Operations ===")
    
    # Create directory
    if not os.path.exists('test_dir'):
        os.makedirs('test_dir')
        print("Directory 'test_dir' created")
    
    # List files in current directory
    print("Files in current directory:")
    for item in os.listdir('.'):
        if os.path.isfile(item):
            print(f"  File: {item}")
        elif os.path.isdir(item):
            print(f"  Directory: {item}")
    
    # Create file in subdirectory
    with open('test_dir/test_file.txt', 'w') as file:
        file.write("This is a test file in a subdirectory")
    
    print("Test file created in subdirectory")

# ===============================
# 🛡️ ERROR HANDLING
# ===============================

def safe_file_operations():
    """Safe file operations with proper error handling"""
    
    print("\n=== Safe File Operations ===")
    
    # Safe reading
    try:
        with open('nonexistent.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found - creating it...")
        with open('nonexistent.txt', 'w') as file:
            file.write("This file was created because it didn't exist")
    except PermissionError:
        print("Permission denied to read file")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Safe writing
    try:
        with open('test_write.txt', 'w') as file:
            file.write("Test content")
        print("File written successfully")
    except PermissionError:
        print("Permission denied to write file")
    except Exception as e:
        print(f"Unexpected error: {e}")

# ===============================
# 🎯 PRACTICAL EXAMPLE: LOG FILE HANDLER
# ===============================

import datetime

class LogHandler:
    """Simple log file handler"""
    
    def __init__(self, log_file='app.log'):
        self.log_file = log_file
    
    def log(self, message, level='INFO'):
        """Write log message to file"""
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        with open(self.log_file, 'a') as file:
            file.write(log_entry)
    
    def read_logs(self, lines=None):
        """Read log entries"""
        try:
            with open(self.log_file, 'r') as file:
                if lines:
                    # Read last n lines
                    all_lines = file.readlines()
                    return all_lines[-lines:]
                else:
                    return file.readlines()
        except FileNotFoundError:
            return []
    
    def clear_logs(self):
        """Clear all logs"""
        with open(self.log_file, 'w') as file:
            file.write("")
        print("Logs cleared")

def demonstrate_log_handler():
    """Demonstrate the log handler"""
    
    print("\n=== Log Handler Demo ===")
    
    # Create log handler
    logger = LogHandler('demo.log')
    
    # Write some logs
    logger.log("Application started")
    logger.log("User logged in", "INFO")
    logger.log("Database connection failed", "ERROR")
    logger.log("User performed action", "DEBUG")
    logger.log("Application shutdown", "INFO")
    
    print("Logs written to 'demo.log'")
    
    # Read logs
    print("\nAll logs:")
    logs = logger.read_logs()
    for log in logs:
        print(f"  {log.strip()}")
    
    # Read last 3 logs
    print("\nLast 3 logs:")
    recent_logs = logger.read_logs(3)
    for log in recent_logs:
        print(f"  {log.strip()}")

# ===============================
# 🏭 UTILITY FUNCTIONS
# ===============================

def create_sample_file():
    """Create a sample file for testing"""
    
    content = """This is a sample text file.
It contains multiple lines of text.
This file is used for demonstrating file handling in Python.
Each line can be read separately or the entire file can be read at once.
File handling is an important concept in programming."""
    
    with open('sample.txt', 'w') as file:
        file.write(content)
    
    print("Sample file 'sample.txt' created!")

def cleanup_files():
    """Clean up test files"""
    
    print("\n=== Cleanup ===")
    
    files_to_remove = [
        'output.txt', 'lines.txt', 'append_demo.txt',
        'students.csv', 'students.json', 'sample_renamed.txt',
        'test_write.txt', 'demo.log'
    ]
    
    for filename in files_to_remove:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed: {filename}")
    
    # Remove test directory
    if os.path.exists('test_dir'):
        shutil.rmtree('test_dir')
        print("Removed: test_dir")

# ===============================
# 🚀 MAIN EXECUTION
# ===============================

if __name__ == "__main__":
    print("🐍 Python File Handling Examples")
    print("=" * 50)
    
    # Create sample file first
    create_sample_file()
    
    # Demonstrate all file operations
    read_file_basic()
    read_file_line_by_line()
    read_file_into_list()
    read_file_with_encoding()
    
    write_file_basic()
    write_file_line_by_line()
    append_to_file()
    
    create_csv_file()
    read_csv_file()
    read_csv_as_dict()
    
    create_json_file()
    read_json_file()
    
    file_operations()
    directory_operations()
    
    safe_file_operations()
    demonstrate_log_handler()
    
    # Cleanup (uncomment to remove test files)
    # cleanup_files()
    
    print("\n" + "=" * 50)
    print("✅ File handling examples completed!")
    print("📁 Check the created files in your directory")
